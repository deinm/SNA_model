from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/Users/deinm/Downloads/chromedriver')
driver.implicitly_wait(3)
base_URL = 'https://models.com/rankings/ui/infinite/Runway-All/'

# login
driver.get('https://models.com/account/')
driver.implicitly_wait(1)
loginID = 'deinm@naver.com'
loginPW = 'Serenity99!'

driver.find_element_by_xpath('//*[@id="LoginUSERID"]').send_keys(loginID)
driver.find_element_by_name('PASSWORD').send_keys(loginPW)
driver.find_element_by_name('loginB').click()

data_dict = {}

for i in range(1,241,10):
    URL = base_URL + str(i)
    driver.get(URL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    names = soup.find_all('div', {'class': 'small-12 medium-3 columns showtotals'})
    # print(names)

    model_url = []
    model_namelist = []
    nameindex = 0

    for name in names:
        model_url.append(name.find('h3').find('a')['href'])
        model_namelist.append(name.find('h3').text)

    for single_url in model_url:
        index = 1
        while True:
            show_url = single_url + '/' + str(index) + '/year/all'
            driver.get(show_url)
            driver.implicitly_wait(1)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            check = soup.find('div',{'class':'userInfoMessageDiv'})
            if check is not None:
                break

            shows = soup.find('div', {'class': 'active-tab-body'})
            shows = shows.find_all('div',{'class':'row'})

            for single_show in shows:
                data = single_show.find('div',{'class':'small-9 columns'})
                showname = data.find('a').text
                credit = single_show.find_all('div',{'class':'credits'})
                if len(credit)>1:
                    for single_credit in credit:
                        if 'Exclusive' in single_credit.text:
                            if model_namelist[nameindex] in data_dict:
                                data_dict[model_namelist[nameindex]].append(showname)
                            else:
                                data_dict[model_namelist[nameindex]] = [showname]

                            print(model_namelist[nameindex],showname,single_credit.text)

            index+=1

        nameindex+=1
    break

print(data_dict)

with open('exclusive_2020SS.csv','w') as f:
    for key, values in data_dict.items():
        print(values)
        values = str(values)[1:-1]
        values = values.split(',')
        final = []
        for single_value in values:
            final.append(single_value.strip()[1:-1])

        f.write(str(key)+","+','.join(final)+'\n')