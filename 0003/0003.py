# -*- coding: utf-8 -*-
#将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

import redis
import os

def store_codes(file='codes.txt'):
    conn = redis.StrictRedis()
    conn.config_set('dir', os.getcwd())
    conn.config_set('dbfilename', 'dump.rdb')

    with open(file, 'rb') as f:
        for line in f.readlines():
            code = line.strip()
            conn.sadd('codes', code)
    conn.save()

if __name__ == '__main__':
    store_codes(file='codes.txt')
