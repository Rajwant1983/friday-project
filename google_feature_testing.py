from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\\Users\\pilly\\Downloads\\chromedriver_win32\\chromedriver') 
driver.maximize_window()
queries=['Netflix series','Movies']#,'hollywood movies','iron man','titanic','avengers',infinity war','lion king','beauty and the beast'
result=[] 
for query in queries:
 driver.get('https://www.google.co.uk')
 reject_class=driver.find_elements(By.CLASS_NAME,'tHlp8d')
 for reject_button in reject_class:
    print(reject_button.text)
    if reject_button.text =='Reject all':
        reject_button.click()
search_box_element=driver.find_element_by_class_name('gLFyf')
search_box_element.send_keys(query)
time.sleep(3)
submit_button_element=driver.find_element_by_class_name('gNO89b')
submit_button_element.click()
try:
    find_headline=driver.find_element_by_class_name('span.REySof')
    if 'Movies' in find_headline.text:
        result.append(True)
    else:
        result.append('False')
except:
    result.append('False')       
driver.close()
print(result)