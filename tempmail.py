#Task 1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
import time
import random
keyboard = Controller()

url = 'https://temp-mail.org/en/'
service = Service("C:/Users/User/Downloads/chromedriver.exe")
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

driver.find_element(By.ID, 'mail').click()
time.sleep(random.randint(15,20))
with keyboard.pressed(Key.ctrl):
    keyboard.press('a')
    keyboard.release('a')
with keyboard.pressed(Key.ctrl):
    keyboard.press('c')
    keyboard.release('c')

time.sleep(random.randint(1,3))


driver.close()