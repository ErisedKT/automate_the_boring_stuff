#! /usr/bin/python3
# urlRegex.py - Finds URLs on the clipboard.

import pyperclip, re

urlRegex = re.compile(r'''(
    (http://|https://)
    (www\.)?
    ([a-zA-Z0-9@:%._\+~#=]{2,256})+
    (\.[a-zA-Z]{2,4})
    (/)?
    (\w+)?   
    )''', re.VERBOSE)
text = str(pyperclip.paste())
matches = []
for groups in urlRegex.findall(text):
    matches.append(groups[0])
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No URLs found.')