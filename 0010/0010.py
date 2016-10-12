# -*- coding: utf-8 -*-
#使用 Python 生成类似于下图中的字母验证码图片

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import string
import random

def generate(length=4):
    width, height = 240, 60

    img = Image.new('RGB', (width, height), (200, 200, 200))
    font = ImageFont.truetype('Arial.ttf', 50)
    draw = ImageDraw.Draw(img)

    for _ in range(3000):
        fill_color = tuple(random.randint(30, 100) for _ in range(3))
        draw.point((random.randint(0, width), random.randint(0, height)), fill=fill_color)

    for idx, char in enumerate([random.choice(string.ascii_letters + string.digits) for _ in range(4)]):
        fill_color = tuple(random.randint(30, 100) for _ in range(3))
        draw.text((60 * idx + 20, 5), char, font=font, fill=fill_color)

    img = img.filter(ImageFilter.BLUR)
    img.save('output.jpg')

if __name__ == '__main__':
    generate()
