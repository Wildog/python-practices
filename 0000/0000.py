# -*- coding: utf-8 -*-
#将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def add_num(im, text='0'):
    width, _ = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('Arial.ttf', size=width / 3)
    draw.text((width * 2 / 3, 0), text, font=font, fill='#ff0000')
    im.save('out.png', 'png')

if __name__ == '__main__':
    im = Image.open("in.png")
    add_num(im, '5')
