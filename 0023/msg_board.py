# -*- coding: utf-8 -*-
from flask import Flask, make_response, request, render_template, redirect
from datetime import datetime
import redis
import json
import os

app = Flask(__name__, static_path='/static', template_folder='.')

@app.route('/')
def index():
    msgs = conn.lrange('msg', 0, -1)
    msgs = [json.loads(msg) for msg in msgs]
    page = render_template('index.html', msgs=msgs, msg_count=len(msgs))
    res = make_response(page)
    return res

@app.route('/submit', methods=['POST'])
def new_msg():
    name = request.form['name']
    msg = request.form['msg']
    if name == '' or msg == '':
        return 'Name or message cannot be empty!'
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    record = {'name': name, 'msg': msg, 'time': time}
    conn.lpush('msg', json.dumps(record))
    return redirect('/')

def init_db():
    global conn
    conn = redis.StrictRedis()
    conn.config_set('dir', os.getcwd())
    conn.config_set('dbfilename', 'msg.rdb')
    conn.config_set('save', '10 1')

if __name__ == '__main__':
    init_db()
    app.run('0.0.0.0', 5000, debug=True)
