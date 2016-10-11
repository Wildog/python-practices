# -*- coding: utf-8 -*-
#你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

from word_count import word_count
from itertools import takewhile
import os

def words_of_diaries(dir='diaries'):
    for file in os.listdir(os.path.join(os.getcwd(), dir)):
        counter = word_count(os.path.join(os.getcwd(), dir, file))
        results = sorted(counter, key=lambda k: counter[k], reverse=True)
        maxes = list(takewhile(lambda e: counter[e] == counter[results[0]], results))
        print file, ':', maxes

if __name__ == '__main__':
    words_of_diaries()
