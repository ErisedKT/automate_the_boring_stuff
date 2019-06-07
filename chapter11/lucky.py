#! /usr/bin/python3
# lucky.py - Opens several Google search results.

import webbrowser, sys, requests, bs4, logging

res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
print('Googling...')   # display text while downloading the Google page
res.raise_for_status()

# Retrieve top search result links.

soup = bs4.BeautifulSoup(res.text, features='html.parser')
 
# Open a browser tab for each result.

linkElems = soup.select('.jfp3ef > a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://www.google.com' + linkElems[i].get('href'))