from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd
import numpy as np
import collections as co
import time
import re

data = pd.DataFrame(data=[], columns=['리뷰', '별점', '날짜'])


driver = webdriver.Chrome("chromedriver.exe")
url = "https://play.google.com/store/apps/details?id=com.coupang.mobile&showAllReviews=true"
driver.get(url)


def next_page():
    driver.find_element_by_xpath(
        '//div[@class="pf5lIe"]/div[@role="img"]').click()


def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, 999999999999)")
    time.sleep(2)


def crawl(driver, data):

    # 리뷰, 별점, 날짜 수집
    reviews = driver.find_elements_by_css_selector('.UD7Dzf')
    star_grades = driver.find_elements_by_xpath(
        '//div[@class="pf5lIe"]/div[@role="img"]')
    dates = driver.find_elements_by_css_selector('.p2TkOb')

    # k개의 리뷰를 수집합니다.
    i = 0
    k = 0
    while True:
        i += 1
        tmp = []
        tmp.append(reviews[i].text)
        tmp.append(star_grades[i+1].get_attribute('aria-label'))
        tmp.append(dates[i].text)

        # 수집한 1명의 리뷰를 결과 프레임에 추가합니다.
        tmp = pd.DataFrame(data=[tmp], columns=data.columns)
        data = pd.concat([data, tmp])

        if i % 20 == 0:
            prev_height = browser.execute_script(
                "return document.body.scrollHeight")
            croll_down(driver)
            curr_height = browser.execute_script(
                "return document.body.scrollHeight")
            if prev_height == curr_height:
                try:
                    driver.find_element_by_xpath(
                        '//div[@class="pf5lIe"]/div[@role="img"]').click()
                except:
                    pass

        if i % 100 == 0:
            data.reset_index(inplace=True, drop=True)
            tmp = data.copy()
            tmp['별점'] = tmp['별점'].apply(lambda x: x[5:])
            tmp.head(3)
            m = re.compile('[0-9][\.0-9]*')
            tmp['별점'] = tmp['별점'].apply(lambda x: m.findall(x)[0])
            tmp.to_csv(f'쿠팡_리뷰_평점_{k}.csv', encoding='utf-8')

    # return data


data = crawl(driver, data)
