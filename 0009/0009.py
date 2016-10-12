# -*- coding: utf-8 -*-
#一个HTML文件，找出里面的链接。

import urllib2
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://www.douban.com'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    for a in soup.find_all('a'):
        print a
