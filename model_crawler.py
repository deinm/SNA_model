from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/Users/deinm/Downloads/chromedriver')
driver.implicitly_wait(3)

# scroll down
'''
URL = 'https://models.com/rankings/ui/infinite/Runway-All/'
driver.get(URL)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

elem = driver.find_element_by_tag_name('body')
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
'''

base_URL = 'https://models.com/rankings/ui/infinite/Runway-All/'

model_namelist = []
model_walklist = []
model_ocnumlist = []
model_nationallist = []
model_personallist = []

for i in range(1,241):
    URL = base_URL + str(i)
    driver.get(URL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    names = soup.find_all('div',{'class':'small-12 medium-3 columns showtotals'})

    model_url = []

    for name in names:
        model_url.append(name.find('h3').find('a')['href'])
        single_name = name.find('h3').text
        data = name.find_all('li')
        walked = data[0].text
        oc_num = 'None'
        if len(data)==2:
            oc_num = data[1].text

        model_namelist.append(single_name)
        model_walklist.append(walked)
        model_ocnumlist.append(oc_num)

    for single_url in model_url:
        driver.get(single_url)
        driver.implicitly_wait(1)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        nationality = 'None'
        try:
            nationality = soup.find('div',{'id':'biodata'}).find('div').text
        except:
            pass

        model_nationallist.append(nationality)

        personal_data = []
        personal_head = []

        try:
            personal_head = soup.find('table',{'id':'cmtable'}).find_all('th')
            tmp_data = soup.find('table',{'id':'cmtable'}).find_all('td')
            for single_data in tmp_data:
                personal_data.append(single_data.text)
        except:
            pass

        personal_dict = {}
        length = len(personal_head)
        if length != 0:
            for index in range(length):
                personal_dict[personal_head[index].text] = personal_data[index]

        model_personallist.append(personal_dict)

    print(model_personallist)