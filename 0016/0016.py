# -*- coding: utf-8 -*-
# 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
#     [
#         [1, 82, 65535], 
#         [20, 90, 13],
#         [26, 809, 1024]
#     ]
# 请将上述内容写到 numbers.xls 文件中

from pyexcel_xls import save_data
import json
import collections

def convert_to_xls(filename):
    with open(filename, 'r') as f:
        sheet = json.load(f, object_pairs_hook=collections.OrderedDict)
        fn = ''.join(filename.split('.')[:-1])
        xls = {fn : sheet}
        save_data(fn + '.xls', xls)

if __name__ == '__main__':
    convert_to_xls('numbers.txt')
