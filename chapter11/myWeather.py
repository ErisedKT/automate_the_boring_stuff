#! /usr/bin/python3
# myWeather.py - Open the browser to the URL for your local weather.
# Usage: myWeather.py <area>

import sys, webbrowser

if len(sys.argv) < 2:
    print('Usage: myWeather.py <area>')
    sys.exit()

area = ' '.join(sys.argv[1:])

webbrowser.open('https://www.google.com/search?q=' + area + ' weather')