# -*- coding: utf-8 -*-
#用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)

from bs4 import BeautifulSoup
import urllib2

def get_image_list(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    for img in soup.select('.d_post_content .BDE_Image'):
        yield img['src']

def download_image(url):
    filename = url.split('/')[-1]
    page = urllib2.urlopen(url)
    with open(filename, 'wb') as f:
        file_size = int(page.info().getheaders('Content-Length')[0])
        print 'Downloading: %s, %s' % (filename, file_size)
        downloaded = 0
        buffer_size = 8192
        while True:
            buffer = page.read(buffer_size)
            if not buffer:
                break
            downloaded += len(buffer)
            f.write(buffer)

if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/2166231880'
    for image_url in get_image_list(url):
        download_image(image_url)
