import os
import random
import string
import json

from pynput.keyboard import Key, Controller
from selenium import webdriver
import time

keyboard = Controller()
browser = webdriver.Chrome(r'C:\Users\dylan\Desktop\Python\Webdriver\chromedriver.exe')

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(2048))

url = 'LINK'

names = json.loads(open('names.json').read())

for name in names:
    browser.get(url)
    time.sleep(7)
    name_extra = ''.join(random.choice(string.digits))
    username = name.lower() + name_extra
    userField = browser.find_element_by_xpath("//*[@id='nickname']")
    userField.send_keys(username)
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(15)
    for x in range(30):
        time.sleep(5)
        pickAnswer = browser.find_element_by_xpath("//*[@id='challenge-game-router']/main/div[2]/div[1]").click()
        time.sleep(5)
        nextButton = browser.find_element_by_xpath("//*[@id='challenge-game-router']/main/button").click()
        time.sleep(5)
        nextNewButton = browser.find_element_by_xpath("//*[@id='challenge-game-router']/div/main/button/span").click()
    browser.quit()
