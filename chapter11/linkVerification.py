#! /usr/bin/python3
# linkVerification.py - Downloads every page on a webpage and prints
# Error 404s as broken links.
# Usage: ./linkVerification.py <foldername> <url>
import requests, os, bs4, sys

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}

# Download webpage. 

res = requests.get(sys.argv[2], headers=headers)
res.raise_for_status()

# Find all links in webpage.

soup = bs4.BeautifulSoup(res.text, 'lxml')
linkElems = [link.get('href') for link in soup.select('a') if link.get('href')]

count = 0   # counts number of links
count_404 = 0   # counts broken links

os.makedirs(sys.argv[1], exist_ok=True) # create folder to put loaded pages in

for link in linkElems:
    try:
        # Download link on webpage.

        res = requests.get(link)
        res.raise_for_status()

        # Write loaded page to file.

        pageFile = open(os.path.join(sys.argv[1], 'link_%s' % (count + 1)), 'wb')
        for chunk in res.iter_content(100000):
            pageFile.write(chunk)

        count += 1  # increment link count
    
    # Handle invalid URLs and broken links.

    except Exception as exc:
        try: 
            # Flag broken links.
            if res.status_code == 404:
                print('Broken link: ' + link)
                count_404 += 1  # increment broken link count
        except:
            continue
print('Found %s working links and %s broken links.' % (count, count_404))