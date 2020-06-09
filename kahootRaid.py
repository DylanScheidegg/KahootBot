import os
import random
import string
import json
from selenium import webdriver
import time

browser = webdriver.Chrome(r'C:\FILEPATH\chromedriver.exe')

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(2048))

url = 'https://kahoot.it/v2/'
game_pin = 'code'
number_quest = 10

names = json.loads(open('names.json').read())

for name in names:
    browser.get(url)
    time.sleep(7)
    game = browser.find_element_by_xpath('/html/body/div/div/div/div/main/div/form/input')
    game.send_keys(game_pin)
    browser.find_element_by_xpath('/html/body/div/div/div/div/main/div/form/button').click()
    time.sleep(5)
    name_extra = ''.join(random.choice(string.digits))
    username = name.lower() + name_extra
    userField = browser.find_element_by_xpath("//*[@id='nickname']")
    userField.send_keys(username)
    browser.find_element_by_xpath('/html/body/div/div/div/div/main/div/form/button').click()
    time.sleep(15)
    for x in range(number_quest):
        time.sleep(5)
        pickAnswer = browser.find_element_by_xpath("//*[@id='challenge-game-router']/main/div[2]/div[1]")
        if browser.find_element_by_xpath(pickAnswer).size['width'] != 0:
            pickAnswer.click()
        else:
            time.sleep(5)
        time.sleep(5)
        nextButton = browser.find_element_by_xpath("//*[@id='challenge-game-router']/main/button")
        if browser.find_element_by_xpath(nextButton).size['width'] != 0:
            nextButton.click()
        else:
            time.sleep(5)
        time.sleep(5)
        nextNewButton = browser.find_element_by_xpath("//*[@id='challenge-game-router']/div/main/button/span")
        if browser.find_element_by_xpath(nextNewButton).size['width'] != 0:
            nextNewButton.click()
        else:
            time.sleep(5)
    browser.quit()
