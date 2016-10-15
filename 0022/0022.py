# -*- coding: utf-8 -*-
# iPhone 6、iPhone 6 Plus 早已上市开卖。请查看你写得 第 0005 题的代码是否可以复用。

from PIL import Image
import os

def batch_resize(dir='inputs', output='outputs', size=[414, 736]):
    for filename in os.listdir(dir):
        img = Image.open(os.path.join(os.getcwd(), dir, filename))
        width, height = img.size

        fw = float(width) / max(size) if width > height else float(width) / min(size)
        fh = float(height) / min(size) if width > height else float(height) / max(size)
        f = max(fw, fh)
        if f > 1:
            img.resize((int(width / f), int(height / f))).save(os.path.join(os.getcwd(), output, filename))

if __name__ == '__main__':
    batch_resize()
