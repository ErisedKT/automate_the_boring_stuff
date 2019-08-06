#! /usr/bin/python
# comicDownloader.py - Checks for Lunar Baboon updates everyday and downloads them.

import requests, bs4, shelve, os, time, threading, math
from urllib.parse import urlparse
from datetime import datetime

def roundup(x):
    return int(math.ceil(x / 15)) * 15

def downloadComic(startPage, endPage):
    url = 'http://www.lunarbaboon.com/comics/?currentPage=' + str(startPage)
    endUrl = 'http://www.lunarbaboon.com/comics/?currentPage=' + str(endPage + 1)
    while url != endUrl:
        while True:
            try:
                res = requests.get(url)
                res.raise_for_status()
                break
            except requests.exceptions.HTTPError:
                print('Waiting for server to allow scraper...')
                time.sleep(5)
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        comicElems = soup.select('.full-image-block > span > img')
        imageUrls = [base_url + urlparse(c.get('src')).path for c in comicElems]
        for imageUrl in imageUrls:
            while True:
                try:
                    res1 = requests.get(imageUrl)
                    res1.raise_for_status()
                    break
                except requests.exceptions.HTTPError:
                    print('Waiting for server to allow scraper...')
                    time.sleep(5)
            imageFile = open(os.path.join('lunarbaboon', 
                             os.path.basename(imageUrl)), 'wb')
            print('Downloading image %s...' % (imageUrl))
            for chunk in res1.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        nextLink = soup.select('.paginationControlNextPageSuffix > a')[0].get('href')
        if nextLink:
            url = base_url + nextLink
        else:
            break

shelf = shelve.open('comic')
os.makedirs('lunarbaboon', exist_ok=True)
url = 'http://www.lunarbaboon.com'
base_url = 'http://www.lunarbaboon.com'
if not shelf.keys():
    res = requests.get(base_url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    shelf['lastDate'] = datetime.strptime(soup.select('.journal-entry-float-date')[0].getText(), '%b%d%Y')
    numPages = int(soup.select('.paginationPageNumber')[-1].getText())
    downloadThreads = []
    for i in range(1, roundup(numPages), 15):
        downloadThread = threading.Thread(target=downloadComic, args=[i, i + 15])
        downloadThreads.append(downloadThread)
        downloadThread.start()
    for downloadThread in downloadThreads:
        downloadThread.join()

else:
    res = requests.get(base_url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    lastDate = shelf['lastDate']
    comicDate = datetime.strptime(soup.select('.journal-entry-float-date')[0].getText(), '%b%d%Y')
    if comicDate > lastDate:
        comicElem = soup.select('.full-image-block > span > img')[0]
        imageUrl = base_url + urlparse(comicElem.get('src')).path
        res = requests.get(imageUrl)
        res.raise_for_status()
        print('Downloading image %s...' % (imageUrl))
        imageFile = open(os.path.join('lunarbaboon', 
                         os.path.basename(imageUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        shelf['lastDate'] = comicDate

shelf.close()
print('Done.')