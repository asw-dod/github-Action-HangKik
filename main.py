from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# test
import time
import random

driver = webdriver.Chrome()

# 원하는 url로 접속
driver.get('https://forms.gle/ZouR2hTRsZqFVr4X8')
driver.maximize_window()

name = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys("황진주")

number = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
number.send_keys("20193148")

room = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
room.send_keys("B412")

x = random.random(0, 9)


fever = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
fever.send_keys("35.7")

etc = driver.find_element_by_xpath('//*[@id="i21"]/div[3]/div').click()

login_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()
