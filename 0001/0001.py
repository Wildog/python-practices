# -*- coding: utf-8 -*-
#做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random, string

def generate(num, length=12):
    for i in range(num):
        charset = string.ascii_uppercase + string.digits
        code = ''.join([random.choice(charset) for i in range(length)])
        yield code

if __name__ == '__main__':
    with open('codes.txt', 'wb') as f:
        for code in generate(200):
            f.write(code + '\n')
