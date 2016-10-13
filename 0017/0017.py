# -*- coding: utf-8 -*-
# 将第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如下所示：
#     <?xml version="1.0" encoding="UTF-8"?>
#     <root>
#     <students>
#     <!-- 
#         学生信息表
#         "id" : [名字, 数学, 语文, 英文]
#     -->
#     {
#         "1" : ["张三", 150, 120, 100],
#         "2" : ["李四", 90, 99, 95],
#         "3" : ["王五", 60, 66, 68]
#     }
#     </students>
#     </root>

from pyexcel_xls import get_data
from lxml import etree
import json

def xls_to_json_wrapped_by_xml(filename):
    fn = ''.join(filename.split('.')[:-1])
    sheet = get_data(filename)[fn]
    data = {row[0]: row[1:] for row in sheet}
    data_repr = json.dumps(data, ensure_ascii=False)

    root = etree.Element('root')
    comment_node = etree.Comment(u'学生信息表 "id" : [名字, 数学, 语文, 英文]')
    root.append(comment_node)
    data_node = etree.Element(fn)
    data_node.text = data_repr
    root.append(data_node)

    with open(fn + '.xml', 'w') as f:
        f.write(etree.tostring(root, encoding='utf8', pretty_print=True))

if __name__ == '__main__':
    xls_to_json_wrapped_by_xml('student.xls')
