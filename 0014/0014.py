# -*- coding: utf-8 -*-
# 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
#     {
#         "1":["张三",150,120,100],
#         "2":["李四",90,99,95],
#         "3":["王五",60,66,68]
#     }
# 请将上述内容写到 student.xls 文件中

from pyexcel_xls import save_data
import json
import collections

def convert_to_xls(filename):
    with open(filename, 'r') as f:
        data = json.load(f, object_pairs_hook=collections.OrderedDict)
        sheet = [row_data for row_num, row_data in data.items() if row_data.insert(0, row_num) or True]
        fn = ''.join(filename.split('.')[:-1])
        xls = {fn : sheet}
        save_data(fn + '.xls', xls)

if __name__ == '__main__':
    convert_to_xls('student.txt')
