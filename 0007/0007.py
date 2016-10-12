# -*- coding: utf-8 -*-
#有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

import os
import mimetypes

def traverse_dir(path):
    exclude_dirs = ['git']
    for root, dirs, files in os.walk(path):
        root_ext = root.split('.')[-1]
        if root_ext in exclude_dirs:
            continue
        for file in files:
            fp = os.path.join(root, file)
            filetype = mimetypes.guess_type(fp)[0]
            is_text = False if not filetype else filetype.startswith('text')
            if not is_text:
                continue
            yield fp

def count_lines(path):
    lines, blanks, comments = 0, 0, 0
    for fp in traverse_dir(path):
        with open(fp, 'rb') as f:
            for line in f:
                line = line.strip()
                lines += 1
                if line == '':
                    blanks += 1
                elif line.startswith('#') or line.startswith('//'):
                    comments += 1
    return lines, blanks, comments

if __name__ == '__main__':
    stat = count_lines('/Users/pro/Projects/Repo/python-practices')
    print 'lines: %d, blanks: %d, comments: %d' % stat
