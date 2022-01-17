from selenium import webdriver
from selenium.webdriver.common.keys import Keys


path = 'E:\Chromedriver.exe'
driver = webdriver.Chrome(path)


link = 'https://bill.meganet.ru.net/admin/index.cgi?index=150&NAS_ID=1&pg=0&sort=2&desc=DESC'
driver.get(link)

all_session = find_elements(By.XPATH, '//*[@id="INTERNET_ONLINE_"]//*/td[1]/a')


'''
list_of_payment_systems = list(' Банк', ' Payberry', ' RNCB', ' GenBank', '  24Alltime')

for el in list_of_payment_systems:
    fdriver.find_element(By.XPATH, "//td[contains( text( ), el)]").click()
'''


