# -*- coding: utf-8 -*-
# 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。

import os
import hashlib

def hash_pwd(password, salt=None):
    if not salt:
        salt = os.urandom(8)
    if isinstance(password, unicode):
        password = password.encode('utf8')
    result = hashlib.sha512(salt + password).hexdigest()
    result = result + salt
    return result

def check_pwd(inputed, hashed):
    salt = hashed[-8:]
    return hashed == hash_pwd(inputed, salt=salt)

if __name__ == '__main__':
    hashed = hash_pwd('test')
    assert check_pwd('test', hashed)
