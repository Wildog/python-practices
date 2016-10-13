# -*- coding: utf-8 -*-
# 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
#     {
#         "1" : "上海",
#         "2" : "北京",
#         "3" : "成都"
#     }
# 请将上述内容写到 city.xls 文件中

from pyexcel_xls import save_data
import json
import collections

def convert_to_xls(filename):
    with open(filename, 'r') as f:
        data = json.load(f, object_pairs_hook=collections.OrderedDict)
        sheet = [[row_num, row_data] for row_num, row_data in data.items()]
        fn = ''.join(filename.split('.')[:-1])
        xls = {fn : sheet}
        save_data(fn + '.xls', xls)

if __name__ == '__main__':
    convert_to_xls('city.txt')
