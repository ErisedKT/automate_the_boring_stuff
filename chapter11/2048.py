#! /usr/bin/python3
# 2048.py - Plays the 2048 game automatically.

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Open 2014 game in Firefox.

browser = webdriver.Firefox()
browser.get('https://play2048.co/')

# Find body tag to send keys to.

gridElem = browser.find_element_by_tag_name('body')

arrows = [Keys.ARROW_UP, Keys.ARROW_RIGHT, Keys.ARROW_DOWN, Keys.ARROW_LEFT]
count = 0   # counts keystrokes

# Tracks game status.

gameStatusElem = browser.find_element_by_css_selector('.game-container p')

# Send keys while game isn't over.

while gameStatusElem.text != 'Game over!':
    gridElem.send_keys(arrows[count % 4])
    count += 1

# Find score in page.
score = browser.find_element_by_class_name('score-container').text
print('Game Over!')

# Print score.
print('Your score was: ' + score)           