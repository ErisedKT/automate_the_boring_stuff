#! /usr/bin/python3
# openImgur.py - Opens several Imgur search results.

import sys, webbrowser, bs4, requests

print('Searching Imgur for ' + ' '.join(sys.argv[1:]) + '...')
res = requests.get('https://imgur.com/search?q=' + ' '.join(sys.argv[1:]))
soup = bs4.BeautifulSoup(res.text, 'html.parser')

linkElems = soup.select('.post a')
numOpen = min(5, len(linkElems))

for i in range(numOpen):
    webbrowser.open('https://imgur.com' + linkElems[i].get('href'))