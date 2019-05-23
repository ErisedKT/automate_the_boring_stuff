#! /usr/bin/python3
# madLibs.py - Lets user add text anywhere the word 
# ADJECTIVE, NOUN, ADVERB, or VERB appears in the text
# file

import os, re

textFilePath = input('Enter text file path: ')
while not os.path.exists(textFilePath):
    print('This file does not exist. Try again!')
    exit()

textFile = open(textFilePath)
newFile = open('newFile.txt', 'w')
text = textFile.read()[:-1]
wordRegex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
matches = wordRegex.findall(text)
for m in matches:
    article = 'a'
    if m == 'ADJECTIVE' or m == 'ADVERB':
        article = 'an'
    print('Enter %s %s:' % (article, m.lower()))
    sub = input()
    text = text.replace(m, sub, 1)
print(text)
newFile.write(text)
textFile.close()
newFile.close()
