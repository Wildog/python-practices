# -*- coding: utf-8 -*-
#敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

def filter_word(list_file='filtered_words.txt'):
    word_list = []
    with open(list_file, 'rb') as f:
        for line in f.readlines():
            word_list.append(line.strip())
    input_text = raw_input('> ')
    for word in word_list:
        if word in input_text:
            input_text = input_text.replace(word, '*' * len(word.decode('utf-8')))
    print input_text

if __name__ == '__main__':
    filter_word()
