from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


path = 'E:\Chromedriver.exe'
driver = webdriver.Chrome(path)


link = 'https://bill.meganet.ru.net/admin/index.cgi?index=150&NAS_ID=1&pg=0&sort=2&desc=DESC'
driver.get(link)

all_session = find_elements(By.XPATH, '//*[@id="INTERNET_ONLINE_"]//*/td[1]/a')


# for loop in func_bill 

from datetime import datetime, timedelta, date

today = date.today()

date_str = '2022-01-17'
date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()

while date_obj <= today:
    print(date_obj)
    date_obj = date_obj + timedelta(days = 1)


