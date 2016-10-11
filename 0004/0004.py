# -*- coding: utf-8 -*-
#任一个英文的纯文本文件，统计其中的单词出现的个数。

import re
import string
from collections import defaultdict

def word_count(file='text.txt'):
    counter = defaultdict(lambda: 0)

    with open(file, 'r') as f:
        content = f.read()
        results = re.findall('\S+', content)
        for result in results:
            word = result.strip(string.punctuation).lower()
            if word: counter[word] += 1

    return counter

if __name__ == '__main__':
    counter = word_count('text.txt')
    for word, freq in counter.items():
        print word, ':', freq
