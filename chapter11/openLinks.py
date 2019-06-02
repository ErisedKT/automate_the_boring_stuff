#! /usr/bin/python3
# openLinks.py - Opens all the links on a page in separate browser tabs.
# Usage: openLinks.py <filename> OR openLinks 

import sys, re, webbrowser, pyperclip, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

logging.debug('Start of program.')
urlRegex = re.compile(r'''
    (http[s]?://)
    (www\.)?
    ([-a-zA-Z0-9@:%_\+\.~#=]{2,256})
    (\.[a-z]{2,4})
    (/\w+)*
    ''', re.VERBOSE)

contents = ''
if len(sys.argv) == 2:
    with open(sys.argv[1]) as txtFile:  
        contents = txtFile.read()
else:
    contents = pyperclip.paste()
logging.debug('contents contains: ' + contents)

links = urlRegex.finditer(contents)
logging.debug('Links found in text are: ' + len(links))
for link in links:
    webbrowser.open(link.group())
    logging.debug('Opening ' + link.group())
logging.debug('End of program.')