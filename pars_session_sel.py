from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


path = 'E:\Chromedriver.exe'
driver = webdriver.Chrome(path)


link = 'https://bill.meganet.ru.net/admin/index.cgi?index=150&NAS_ID=1&pg=0&sort=2&desc=DESC'
driver.get(link)

all_session = find_elements(By.XPATH, '//*[@id="INTERNET_ONLINE_"]//*/td[1]/a')


# -------------
from datetime import datetime, timedelta, date

date_bill = {'first_date':date_obj, 'last_date':today}

def report_billing(date):
    # ...

    while date[first_date] <= date[last_date]:

        #func: func_name(date[first_date])

       date[first_date] = date[first_date] + timedelta(days = 1)


# -------------
# dataclass for report
from dataclasses import dataclass
from typing import Dict

@dataclass
class BillingReport:
    billing_data: Dict[str, int]
        
    def report(self) -> str:
        repReq = f'Заявки - {self.billing_data["dayReq"]}/{self.billing_data["periodReq"]}'
        repCon = f'Подключения - {self.billing_data["dayCon"]}/{self.billing_data["periodCon"]}'
        repSumm = f'Сумма - {self.billing_data["daySumm"]}/{self.billing_data["periodSum"]}/{self.billing_data["percent"]}%'
        
        return f'{repReq}\n{repCon}\n{repSumm}'
         
         
bill = {'dayReq':1, 'periodReq':12, 'dayCon': 1, 'periodCon': 12, 'daySumm': 2, 'periodSum': 12, 'percent': 52.3}
result = BillingReport(bill)

print(result.report())