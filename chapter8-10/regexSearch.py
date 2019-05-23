#! /usr/bin/python3
# regexSearch.py - Searches for a user-supplied regex
# in all the .txt files in a folder

# Usage : ./regexSearch.py <folderpath> <regex>

import os, sys, re

if len(sys.argv) != 3:
    print('Usage : ./regexSearch.py <folderpath> <regex>')
    exit()

while not os.path.isdir(sys.argv[1]):
    print('This file does not exist. Try again!')
    exit()

for f in os.listdir(sys.argv[1]):
    if not f.endswith('.txt'):
        continue
    txtFile = open(f)
    reg = re.compile(sys.argv[2])
    text = txtFile.read()
    matches = []
    for match in reg.finditer(text):
        matches.append(match.group())
    if len(matches) != 0:
        print('\n%s matches found in %s!' % (len(matches), f))
        print(matches)
    txtFile.close()