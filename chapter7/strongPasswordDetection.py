#! /usr/bin/python3
# strongPasswordDetection.py - Makes sure password is strong

import re
def validate(text):
    lenRegex = re.compile(r'[A-Za-z0-9@#$%^&+=!()-_,.]{8,}')
    digRegex = re.compile(r'\d')
    lowerRegex = re.compile(r'[a-z]')
    upperRegex = re.compile(r'[A-Z]')
    if lenRegex.search(text) != None and \
        digRegex.search(text) != None and \
        lowerRegex.search(text) != None and \
        upperRegex.search(text) != None:
        print('This is a strong password!')
    else:
        print('This is a weak password.')

validate('Smartwishes@123')
validate('thesis2')
validate('THESEISG')