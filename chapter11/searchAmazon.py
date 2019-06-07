#! /usr/bin/python3
# lucky.py - Opens several Amazon search results.

import webbrowser, sys, requests, bs4, logging

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
print('Searching Amazon for ' + ' '.join(sys.argv[1:]) + '...')
res = requests.get('https://www.amazon.in/s?k=' + '+'.join(sys.argv[1:]), headers=headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.rush-component > a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://amazon.in' + linkElems[i].get('href'))