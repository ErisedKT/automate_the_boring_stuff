#! /usr/bin/python3
# 2048.py - Plays the 2048 game automatically.

import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def gameOver(browser):
    try:
        return browser.find_element_by_css_selector('game-container > game-over')
    except:
        return None

browser = webdriver.Firefox()
browser.get('https://play2048.co/')
gridElem = browser.find_element_by_tag_name('body')
arrows = [Keys.ARROW_UP, Keys.ARROW_RIGHT, Keys.ARROW_DOWN, Keys.ARROW_LEFT]
count = 0
browser.find_element_by_class_name('grid-container').click()
gameStatusElem = browser.find_element_by_css_selector('.game-container p')

while gameStatusElem.text != 'Game over!':
    gridElem.send_keys(arrows[count % 4])
    count += 1

score = browser.find_element_by_class_name('score-container').text
print('Game Over!')
print('Your score was: ' + score)           