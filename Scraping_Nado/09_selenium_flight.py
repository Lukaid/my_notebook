# 0. 패키지 임포트
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 1. 브라우저 실행 및 네이버 항공권으로 이동

browser = webdriver.Chrome()
browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

# 2. 가는날 선택

browser.find_element_by_link_text('가는날 선택').click()  # 가는날 선택 클릭

# 이번달 27, 28일 선택
# browser.find_elements_by_link_text('27')[0].click()
# browser.find_elements_by_link_text('28')[0].click()

# 이러면 다음달
browser.find_elements_by_link_text('27')[0].click()
browser.find_elements_by_link_text('28')[1].click()

# 3. 목적지 제주도 선택

browser.find_element_by_xpath(
    '//*[@id="recommendationList"]/ul/li[1]/div/span').click()

# 4. 항공권 검색 후 맨 첫번째 엘리먼트 정보 가져오기

browser.find_element_by_link_text('항공권 검색').click()
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
# 어떤 엘리먼트가 나올때까지 최대 10초 기다려라
    print(elem.text)
finally:
    browser.quit()
