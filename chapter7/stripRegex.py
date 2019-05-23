#! /usr/bin/python3
# stripRegex.py - Mimics the strip() string method

import re

def stripRegex(text, chars=' '):
    strp = re.compile(r'^[{0}]+|[{0}]+$'.format("".join([re.escape(x) for x in chars])))
    res = strp.sub('', text)
    return res

text1 = '      hello world!        '
text2 = 'xxxxxxbye bye.xxxxxxxxxxxx'
print(stripRegex(text1))
print(stripRegex(text2, 'x'))