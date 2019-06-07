#! /usr/bin/python3
# reviews.py - Opens several reviews for a product on Amazon.

import webbrowser, bs4, requests, sys

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
print('Looking for product...')
res = requests.get(sys.argv[1], headers=headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
reviewElems = soup.select('.review-title-content')

numOpen = min(5, len(reviewElems))
for i in range(numOpen):
    webbrowser.open('https://www.amazon.in' + reviewElems[i].get('href'))