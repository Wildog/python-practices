# -*- coding: utf-8 -*-
#将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import mysql.connector

def store_codes(file='codes.txt'):
    conn = mysql.connector.connect(user='root', password='753951',
                                   host='localhost', database='show_me_the_code')
    cursor = conn.cursor()

    stmt = """
    CREATE TABLE IF NOT EXISTS `codes` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `code` CHAR(12) NOT NULL UNIQUE,
        PRIMARY KEY (`id`)
    );
    """
    cursor.execute(stmt)

    with open(file, 'rb') as f:
        for line in f.readlines():
            code = line.strip()
            try:
                cursor.execute("INSERT INTO `codes` (code) values(%s);", [code])
            except mysql.connector.IntegrityError:
                pass

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    store_codes(file='codes.txt')
