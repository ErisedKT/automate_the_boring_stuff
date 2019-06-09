#! /usr/bin/python3
# cmdLineEmailer.py - Logs into my email account 
# sends an email to the provided address

import sys, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def wait_for_page_load(browser, delay, by, selector):
    try:
        elem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((by, selector)))
        return elem
    except TimeoutException:
        print('Loading took too much time!')

browser = webdriver.Firefox()
browser.get('https://login.yahoo.com/') # Go to Yahoo login page.

# Login using email and password.

emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('not-my-real-email')
nextElem = browser.find_element_by_id('login-signin')
nextElem.click()
passwordElem = wait_for_page_load(browser, 5, By.ID, 'login-passwd')
passwordElem.send_keys('definitely-not-my-real-password')
browser.find_element_by_id('login-signin').send_keys(Keys.ENTER)

# Redirect to Yahoo Mail page.

mailElem = wait_for_page_load(browser, 5, By.ID, 'uh-mail-link')
mailElem.send_keys(Keys.ENTER)

# Click Compose button in mail.

composeBtnElem = wait_for_page_load(browser, 5, By.LINK_TEXT, 'Compose')
composeBtnElem.send_keys(Keys.ENTER)

# Enter recipient's email, subject, and message in fields.

recipientElem = wait_for_page_load(browser, 5, By.ID, 'message-to-field')
recipientElem.send_keys(sys.argv[1])
subElem = browser.find_element_by_css_selector('input[placeholder="Subject"]')
subElem.send_keys('Bot Mail')
contentElem = browser.find_element_by_css_selector('div[aria-label="Message body"]')
contentElem.send_keys(' '.join(sys.argv[2:]))

# Click Send.

browser.find_element_by_css_selector('button[data-test-id="compose-send-button"]').click()
