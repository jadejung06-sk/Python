##### Download Chrome Driver and Prepare for web crawling
## 1. Check chrome Version 
# Web - help - Chrome Info.
# 111.0.5563.147 (64 bit) - Windows
## 2. Down load Selenium with Python - Chrome Driver
# chromedriver.exe
'''
pip install selenium
'''
## 3.1. webdriver.Chrome() Error
# read device interface GUIDs: 지정된 파일을 찾을 수 없습니다. (0x2)    
# DeprecationWarning: executable_path has been deprecated, please pass in a Service object
# >>> https://scribblinganything.tistory.com/463
'''
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(options=options, executable_path=PATH)
'''
## 3.2. driver.find_elements_by_id()
# DeprecationWarning: find_element_by_* commands are deprecated. Please use find_element() instead
# By.ID
# >>> https://dejavuqa.tistory.com/109
'''
from selenium.webdriver.common.by import By
'''