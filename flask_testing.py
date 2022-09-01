from selenium import webdriver
from selenium.webdriver.common.by import By
import time
  

driver = webdriver.Chrome('C:\\Users\\pilly\\Downloads\\chromedriver_win32\\chromedriver') 
time.sleep(3)

driver.get('https://www.google.co.uk')
time.sleep(3)

driver.maximize_window()
time.sleep(3)

driver.close()