# -*- coding: utf-8 -*-
#你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

from PIL import Image
import os

def batch_resize(dir='inputs', output='outputs', size=[568, 1136]):
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
