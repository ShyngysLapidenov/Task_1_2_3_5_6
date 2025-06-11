#Task 1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
import time
import random
import tempmail
import clipboard
import pswrd
keyboard = Controller()
f = open(r"database.txt", "a+")

firstname="Michaelo"
surname= "Obnnkotumpo"
mail= clipboard.paste()
passwrd=pswrd.password
print(passwrd)
day=random.randint(1,30)
day1=str(day)
monthlist=["jan","feb","mar","apr","may","jun","july","aug","sep","oct","no","dec"]
month=random.choice(monthlist)
year=random.randint(1970,2000)
year1=str(year)
f.write(mail+">"+passwrd+">"+day1+":"+month+":"+year1+">"+firstname+">"+surname)
f.close()
#url and drivers

url = 'https://www.facebook.com/r.php?locale=ru_RU&display=page&entry_point=login'
service = Service("C:/Users/User/Downloads/chromedriver.exe")
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)


driver.find_element(By.NAME, 'firstname').send_keys(firstname)
time.sleep(random.randint(1, 5))
driver.find_element(By.NAME, 'lastname').send_keys(surname)
time.sleep(random.randint(1, 5))
driver.find_element(By.NAME, 'reg_email__').send_keys(mail)
time.sleep(random.randint(1, 5) * 0.4)
driver.find_element(By.NAME, 'reg_passwd__').send_keys(passwrd)
time.sleep(random.randint(1, 5) * 0.3)
driver.find_element(By.ID, 'birthday_day').send_keys(day)
time.sleep(random.randint(1, 5) * 0.2)
driver.find_element(By.ID, 'birthday_month').send_keys(month)
time.sleep(random.randint(1, 5) * 0.5)
driver.find_element(By.ID, 'birthday_year').send_keys(year)
time.sleep(random.randint(1, 3))

driver.find_element(By.XPATH, '//input[@value="2"]').click()
time.sleep(random.randint(1, 8))
driver.find_element(By.NAME, "websubmit").click()

time.sleep(20)