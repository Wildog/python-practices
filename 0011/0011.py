# -*- coding: utf-8 -*-
#敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

def filter_word(list_file='filtered_words.txt'):
    word_list = []
    with open(list_file, 'rb') as f:
        for line in f.readlines():
            word_list.append(line.strip())
    input_text = raw_input('> ')
    for word in word_list:
        if word in input_text:
            print 'Human Rights'
            break
    else:
        print 'Freedom'

if __name__ == '__main__':
    filter_word()
