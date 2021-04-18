import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
    "Accept-Language": "ko-KR,ko"  # 이렇게 써줘야 한글 페이지를 반환해줌
}

url = "https://play.google.com/store/apps/details?id=com.coupang.mobile&showAllReviews=true"
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

time.sleep(10)  # 이때 관련성순에서 최신순으로 바꿔주기

data = pd.DataFrame(data=[], columns=['num', 'date',
                    'review', 'rating', 'like'])

k = 0
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    while True:
        try:
            browser.find_element_by_xpath(
                '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div[2]/div').click()
            k += 1
            break
        except:
            browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight - 500)")
            browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)
    if k * 160 >= 1000:
        break


reviews = browser.find_elements_by_css_selector('.UD7Dzf')
star_grades = browser.find_elements_by_xpath(
    '//div[@class="pf5lIe"]/div[@role="img"]')
ddabong = browser.find_elements_by_css_selector('.jUL89d')
dates = browser.find_elements_by_css_selector('.p2TkOb')

for i in range(len(reviews)):
    tmp = []
    tmp.append(i)
    tmp.append(dates[i].text)
    tmp.append(reviews[i].text)
    tmp.append(star_grades[i+1].get_attribute('aria-label'))
    tmp.append(ddabong[i].text)

    tmp = pd.DataFrame(data=[tmp], columns=data.columns)
    data = pd.concat([data, tmp])

data.to_csv('test_data_2.csv', encoding='utf-8-sig')
