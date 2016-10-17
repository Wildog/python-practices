# -*- coding: utf-8 -*-
from flask import Flask, make_response, request, render_template, flash, redirect, session
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import json
import md5
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, static_path='/static', template_folder=basedir)
app.secret_key = u'\x12\x96\x1a\x0e+\xbd\xb4\x1b\x02\xd6G\xe2\xeb\x8f\xf3\xf8f);Us\x05\x84_'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'todolist.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.session_protection = 'basic'
login_manager.login_view = 'login'
login_manager.init_app(app)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(64), primary_key=True, index=True)
    _password = db.Column(db.String(128))
    items = db.relationship('Item')

    @property
    def password(self):
        raise AttributeError('Not readable')

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self._password, password)

    def get_id(self):
        return self.username

class Item(db.Model):
    __tablename__ = 'items'
    itemid = db.Column(db.String(32), primary_key=True)
    username = db.Column(db.String(64), db.ForeignKey('users.username'))
    title = db.Column(db.String())
    description = db.Column(db.Text())
    due = db.Column(db.DateTime())
    created = db.Column(db.DateTime())

@login_manager.user_loader
def load_user(username):
    return User.query.filter_by(username=username).first()

@app.route('/')
@login_required
def index():
    orders = {'title': Item.title, 'due': Item.due, 'created': Item.created}
    order_arg = request.args.get('order', session.get('order', 'title'))
    session['order'] = order_arg
    order = orders.get(order_arg, Item.title)

    search = request.args.get('search')
    page_num = request.args.get('page', 1, type=int)
    if search:
        count = Item.query.filter_by(username=current_user.username).filter(Item.title.like('%' + search + '%')).count()
        pagination = Item.query.filter_by(username=current_user.username).filter(Item.title.like('%' + search + '%')).order_by(order.asc()).paginate(page_num, per_page=5, error_out=True)
    else:
        count = Item.query.filter_by(username=current_user.username).count()
        pagination = Item.query.filter_by(username=current_user.username).order_by(order.asc()).paginate(page_num, per_page=5, error_out=True)
    page = render_template('index.html', username=current_user.username, count=count, items=pagination.items, pagination=pagination, search=search, csrf=session.get('csrf'))

    res = make_response(page)
    return res

@app.route('/delete')
@login_required
def delete():
    print request.args.get('csrf')
    print session.get('csrf')
    if request.args.get('csrf') != session.get('csrf'):
        return 'Illegal operation.'
    itemid = request.args.get('id')
    if itemid is None:
        return 'Illegal operation.'
    item = Item.query.filter_by(username=current_user.username, itemid=itemid).first()
    if item is None:
        return 'Illegal operation.'
    flash('\'' + item.title + '\' deleted')
    db.session.delete(item)
    return redirect('/')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been successfully logged out.')
    return redirect('/login')

class LoginView(MethodView):
    def get(self):
        if current_user.is_authenticated:
            return redirect('/')
        page = render_template('login.html')
        res = make_response(page)
        return res

    def post(self):
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter(func.lower(User.username)==func.lower(username)).first()
        if user is not None and user.verify_password(password):
            login_user(user)
            session['csrf'] = md5.new(os.urandom(24)).hexdigest()
            return redirect('/')
        else:
            flash('Wrong username or password!')
            return redirect('/login')

login_view = LoginView.as_view('login')
app.add_url_rule('/login', view_func=login_view)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    error = False
    if len(username) < 4 or len(username) > 64 or len(password) < 4:
        flash('Invalid format for username or password.')
        error = True
    if User.query.get(username):
        flash('Username already exists.')
        error = True
    if not error:
        user = User(username=username, password=password)
        db.session.add(user)
        flash('You can now login by ' + username + '.')
    return redirect('/login')

@app.route('/newtask', methods=['POST'])
@login_required
def new_task():
    print request.form.get('csrf')
    if request.form.get('csrf') != session.get('csrf'):
        return 'Illegal operation.'
    username = current_user.username
    title = request.form['title']
    description = request.form['description']
    due = request.form['due']
    if title == '' or due == '':
        flash('Title or due time cannot be empty!')
        return redirect('/')
    due = datetime.strptime(due, '%m/%d/%Y %I:%M %p')
    created = datetime.now()
    itemid = md5.new(username.encode('utf8') + title.encode('utf8') + repr(created)).hexdigest()
    item = Item(username=username, itemid=itemid, title=title, due=due, description=description, created=created)
    db.session.add(item)
    flash('New item added.')
    return redirect('/')

@app.template_filter('date_fmt')
def date_fmt(date):
    return datetime.strftime(date, '%m/%d/%Y %-I:%M %p')

if __name__ == '__main__':
    #db.drop_all()
    db.create_all()
    app.run('0.0.0.0', 5000, debug=True)
