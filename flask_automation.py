from http import cookies
from tkinter import BROWSE
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
  

driver = webdriver.Chrome('C:\\Users\\pilly\\Downloads\\chromedriver_win32\\chromedriver') 
driver.maximize_window()

driver.get('https://www.google.com')


#try:
#bottom_element=driver.find_elememt_by_id(pHiOh')
#bottom element =driver.find_element_by_class_name('pHiOh')
bottom_element=driver.find_elements(By.CLASS_NAME,'pHiOh')

driver.manage('QS5gu')
print (bottom_element)
for el in bottom_element:
    if el.text =='Business':
        el.click()
        headline=driver.find_elemets(By.CLASS_NAME,'hero_headline')
        print(headline[0].text)
        break
    #assert bottom_elements[0].text =='About'
    #except:
    #record exception
    print("test failed")

driver.close()