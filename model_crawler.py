from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

def save_data():
    final = pd.DataFrame(model_namelist,columns=['Name'])
    final.insert(1,'Walk',model_walklist,True)
    final.insert(2,'Open',model_opennumlist,True)
    final.insert(3,'Close',model_closenumlist,True)
    final.insert(4,'Nationality',model_nationallist,True)
    final.insert(5,'Profile',model_personallist,True)
    final.insert(6,'Follower', model_followerlist,True)

    print(final)

    final.to_csv('model_2019SS.csv',index=False)

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

# 2020SS
# base_URL = 'https://models.com/rankings/ui/infinite/Runway-All/'

# 2019FW
# base_URL = 'https://models.com/rankings/ui/infinite/Runway-All-2019JanMay/'

# 2019SS
base_URL = 'https://models.com/rankings/ui/infinite/Runway-All-2018JunDec/'
model_namelist = []
model_walklist = []
model_opennumlist = []
model_closenumlist = []
model_nationallist = []
model_personallist = []
model_followerlist = []

for i in range(1,241,10):
    print(i)

    URL = base_URL + str(i)
    driver.get(URL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    names = soup.find_all('div',{'class':'small-12 medium-3 columns showtotals'})
    # print(names)

    model_url = []

    for name in names:
        model_url.append(name.find('h3').find('a')['href'])
        single_name = name.find('h3').text
        data = name.find_all('li')
        walked = data[0].text.split(' ')[2]

        open_num = 0
        close_num = 0

        if len(data)==2:
            oc_num = data[1].text
            oc_num = oc_num.split(' ')
            oc_num = oc_num[1].split('/')
            open_num = oc_num[0]
            close_num = oc_num[1]

        model_namelist.append(single_name)
        model_walklist.append(walked)
        model_opennumlist.append(open_num)
        model_closenumlist.append(close_num)

    for single_url in model_url:
        driver.get(single_url)
        driver.implicitly_wait(1)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        nationality = 'None'
        try:
            nationality = soup.find('div',{'id':'biodata'}).find('div').text
            nationality = nationality.split(':')[1].strip()
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

        # print(model_personallist)

        try:
            follower = soup.find('div',{'id':'socialLinks'}).find('li').text.strip()
            # print(follower)
            model_followerlist.append(follower)
        except:
            model_followerlist.append('-')

    if i%10==1:
        print("Saved",i)
        save_data()

save_data()