# -*- coding: utf-8 -*-
# 将第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下所示：
#     <?xml version="1.0" encoding="UTF-8"?>
#     <root>
#     <numbers>
#     <!-- 
#         数字信息
#     -->
#     [
#         [1, 82, 65535],
#         [20, 90, 13],
#         [26, 809, 1024]
#     ]
#     </numbers>
#     </root>

from pyexcel_xls import get_data
from lxml import etree
import json

def xls_to_json_wrapped_by_xml(filename):
    fn = ''.join(filename.split('.')[:-1])
    sheet = get_data(filename)[fn]
    data_repr = json.dumps(sheet, ensure_ascii=False)

    root = etree.Element('root')
    comment_node = etree.Comment(u'数字信息')
    root.append(comment_node)
    data_node = etree.Element(fn)
    data_node.text = data_repr
    root.append(data_node)

    with open(fn + '.xml', 'w') as f:
        f.write(etree.tostring(root, encoding='utf8', pretty_print=True))

if __name__ == '__main__':
    xls_to_json_wrapped_by_xml('numbers.xls')
