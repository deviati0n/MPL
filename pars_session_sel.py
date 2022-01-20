from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


path = 'E:\Chromedriver.exe'
driver = webdriver.Chrome(path)


link = 'https://bill.meganet.ru.net/admin/index.cgi?index=150&NAS_ID=1&pg=0&sort=2&desc=DESC'
driver.get(link)

all_session = find_elements(By.XPATH, '//*[@id="INTERNET_ONLINE_"]//*/td[1]/a')


# -------------
from pprint import pprint

import requests
from lxml import html

headers = {'Content-Type': 'text/html',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                         'Version/13.1.1 Safari/605.1.15'}


def connect(link):
    response = requests.get(link, headers=headers)
    print(response)

    return html.fromstring(response.content)


def find_all_pro(tree_x):
    pro_player = tree_x.xpath('//*[@id="tabs-1"]/div/table/tbody/tr[*]/td[1]/a/@href')
    return pro_player


url = "https://dota2protracker.com/"
tree = connect(url)
list_of_pro = find_all_pro(tree)
# pprint(list_of_pro)
for link_ in list_of_pro:
    new_link = link_.replace(' ', '%20') or link_.replace('^', '%5E')
    print(url + new_link)








