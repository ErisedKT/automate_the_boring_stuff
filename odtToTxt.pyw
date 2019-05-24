#! /usr/bin/python3
# odtToTxt.py - Copies contents of /home/sanya/python_notes.odt to
# /home/sanya/atbswp/python_notes.txt

# Usage: ./odtToTxt 

import sys, numpy

if len(sys.argv) != 1:
    print('Usage: ./odtToTxt')
    sys.exit()

src = open('/home/sanya/python_notes.odt')
dest = open('/home/sanya/atbswp/python_notes.txt', 'w')

contents = src.read()
dest.write(contents)

src.close()
dest.close()