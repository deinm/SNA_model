import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/Users/deinm/Downloads/chromedriver')
driver.implicitly_wait(3)

URL = 'https://models.com/rankings/ui/Runway/'
driver.get(URL)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

elem = driver.find_element_by_tag_name('body')
print(elem)
elem.send_keys(Keys.END)

pagedowns = 1
# 스크롤을 20번 진행한다.
while pagedowns < 72:
        # PAGE_DOWN(스크롤)에 따라서 결과 값이 달라진다.
        # 기본적으로 브라우저 조작을 통해 값을 얻어올 때는 실제 브라우저에 보이는 부분이어야 요소를 찾거나 특정 이벤트를 발생시킬 수 있다.
        elem.send_keys(Keys.PAGE_DOWN)
        # 페이지 스크롤 타이밍을 맞추기 위해 sleep
        time.sleep(1)
        pagedowns+=1

names = soup.find_all('div',{'class':'small-12 medium-3 columns showtotals'})

for name in names:
    single_name = name.find('h3').text
    data = name.find_all('li')
    walked = data[0].text
    oc_num = 'None'
    if len(data)==2:
        oc_num = data[1].text
    print(single_name,walked,oc_num)
    print("@")