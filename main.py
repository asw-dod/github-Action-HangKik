import os
from datetime import datetime
from pytz import timezone

import time
import random


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from github import Github
def get_github_repo(access_token, repository_name):
    g = Github(access_token)
    repo = g.get_user().get_repo(repository_name)
    return repo


def upload_github_issue(repo, title, body):
    repo.create_issue(title=title, body=body)

access_token = os.environ['GITHUB_TOKEN']
repository_name = "github-Action-HangKik"

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("lang=ko_KR")
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("--no-sandbox")

# chrome driver
driver = webdriver.Chrome('chromedriver', chrome_options=options)
def call(name, number, room, temperture):
    # 원하는 url로 접속
    driver.get('https://forms.gle/ZouR2hTRsZqFVr4X8')
    driver.maximize_window()
    name = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name.send_keys(name)
    number = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    number.send_keys(number)
    room = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    room.send_keys(room)
    fever = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fever.send_keys(temperture)
    etc = driver.find_element_by_xpath('//*[@id="i21"]/div[3]/div').click()
    login_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()


def makeBody(list):
    result = ""
    for item in list:
        result += f"이름 : {item[0]}, 학번 : {item[1]}, 방번호 : {item[2]}, 체온 : {item[3]}\n"
    return result



seoul_timezone = timezone('Asia/Seoul')
today = datetime.now(seoul_timezone)
today_data = today.strftime("%Y년 %m월 %d일 %H시 %M분 : %S초")


students = [ [ "차주형", "20183221", "B412" ] ]

for student in students:
    temp = rand.randrange(36.0, 37.0)
    student.append(temp)
    call(student[0], student[1], student[2], temp)

repo = get_github_repo(access_token, repository_name)
title = f"날짜 발열 테스트 : ({today_data})"

body = makeBody(students)

upload_github_issue(repo, title, body)