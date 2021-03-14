import os
from datetime import datetime
from pytz import timezone
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from github import Github

students = [["황진주", "20193148", "B424"], ["남유정", "20193166", "B344"], ["정현수", "20193146", "A419"], ["김태연", "20190511", "B424"], ["박근민", "20213056", "A1028"]]

def get_github_repo(access_token, repository_name):
    g = Github(access_token)
    repo = g.get_user().get_repo(repository_name)
    return repo

def upload_github_issue(repo, title, body):
    repo.create_issue(title=title, body=body)

def delete_github_issue(repo):
    issues = repo.get_issues(state='open')
    for issue in issues:
        if "날짜 발열 테스트" in issue.title:
            issue.edit(state='closed')
            print(issue.title)


githubCall = False
if 'GITHUB_TOKEN' in os.environ:
    access_token = os.environ['GITHUB_TOKEN']
    githubCall = True
	

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


def call(username, usernumber, userroom, temperture):
    # 원하는 url로 접속
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdka3B7OA0l1aj7H26bPkNynKzHaH2PahuRNdbqGpyEepCX3w/viewform')
    driver.maximize_window()
    name = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name.send_keys(username)
    number = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    number.send_keys(usernumber)
    room = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    room.send_keys(userroom)
    # 랜덤 체온
    fever = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fever.send_keys(temperture)
    etc = driver.find_element_by_xpath('//*[@id="i22"]/div[2]').click()
    login_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()
    return

def makeBody(list):
    result = ""
    for item in list:
        result += f"이름 : {item[0]}, 학번 : {item[1]}, 방번호 : {item[2]}, 체온 : {item[3]}\n"
    return result

seoul_timezone = timezone('Asia/Seoul')
today = datetime.now(seoul_timezone)
today_data = today.strftime("%Y년 %m월 %d일 %H시 %M분 : %S초")

for student in students:
    temp = random.randrange(0, 8)
    temp = 36 + (temp / 10)
    temp = str(temp)
    student.append(temp)
    call(student[0], student[1], student[2], temp)

if githubCall:
    repo = get_github_repo(access_token, repository_name)
    delete_github_issue(repo)
        
    title = f"날짜 발열 테스트 : ({today_data})"
    body = makeBody(students)
    upload_github_issue(repo, title, body)
