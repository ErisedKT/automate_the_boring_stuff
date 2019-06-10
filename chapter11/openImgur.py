#! /usr/bin/python3
# openImgur.py - Opens several Imgur search results.
# Usage: ./openImgur.py <numberOfResults> <search category>

import sys, webbrowser, bs4, requests, os

print('Searching Imgur for ' + ' '.join(sys.argv[2:]) + '...')

# Download search results page.

res = requests.get('https://imgur.com/search?q=' + ' '.join(sys.argv[2:]))
res.raise_for_status()

# Create folder to put search results in.

folderName = '_'.join(sys.argv[2:])
print('Created folder %s...' % folderName)
os.makedirs(folderName, exist_ok=True)

# Look for results in page.

soup = bs4.BeautifulSoup(res.text, 'lxml')
linkElems = soup.select('.post a')

# Find number of images to put in files.

numOpen = min(int(sys.argv[1]), len(linkElems))

for i in range(numOpen):
    print('Downloading result %s...' % (i + 1))

    # Download page for individual search result.

    url = 'https://imgur.com' + linkElems[i].get('href')
    res = requests.get(url)
    res.raise_for_status()

    # Find image source in page.

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    imgElem = soup.select('link[rel="image_src"]')

    # Download image.

    imgUrl = imgElem[0].get('href')
    res = requests.get(imgUrl)
    res.raise_for_status()

    # Write image to file.
    
    imageFile = open(os.path.join(folderName, os.path.basename(imgUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

print('Done.')