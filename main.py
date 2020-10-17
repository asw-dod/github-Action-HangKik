import os
from datetime import datetime
from pytz import timezone
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# test
import time
import random
from github import Github

def get_github_repo(access_token, repository_name):
    g = Github(access_token)
    repo = g.get_user().get_repo(repository_name)
    return repo


def upload_github_issue(repo, title, body):
    repo.create_issue(title=title, body=body)


seoul_timezone = timezone('Asia/Seoul')
today = datetime.now(seoul_timezone)
today_data = today.strftime("%Y년 %m월 %d일 %H시 %M분 : %S초")

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

# 원하는 url로 접속
driver.get('https://forms.gle/ZouR2hTRsZqFVr4X8')
driver.maximize_window()

name = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys("차주형")

number = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
number.send_keys("20193148")

room = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
room.send_keys("B412")

x = random.randrange(0, 9)


fever = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
fever.send_keys("35.7")

etc = driver.find_element_by_xpath('//*[@id="i21"]/div[3]/div').click()

login_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()



repo = get_github_repo(access_token, repository_name)

title = f"날짜 발열 테스트 : ({today_data})"
body = "코드가 여기까지 돌았다면. 정상적으로 동작을 하였습니다. \n없다면 직접하시길 바랍니다. !!"

upload_github_issue(repo, title, body)