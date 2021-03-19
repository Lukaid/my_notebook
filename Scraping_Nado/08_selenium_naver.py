# 1. 네이버로 이동

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://naver.com")


# 2. 로그인 하기

browser.find_element_by_class_name('link_login').click()

# 3. ID, PW 입력

browser.find_element_by_id('id').send_keys('naver_id')
browser.find_element_by_id('pw').send_keys('wrong_pw')

# 4. 로그인 버튼 클릭

browser.find_element_by_id('log.login').click()

time.sleep(3) # 로딩시간 3초정도 기다려 주기

# 5. ID를 새로 입력하고 싶으면

browser.find_element_by_id('id').clear() # 원래 적혀있는 아이디 지우기
browser.find_element_by_id('id').send_keys('my_id')

# 6. html 정보 출력

print(browser.page_source)

# 7. 브라우저 닫기

browser.quit()
