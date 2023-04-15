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
## 3.3. wait
# >>> https://selenium-python.readthedocs.io/waits.html
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    driver.find_element(by = By.ID, value = "divHeaderSearch").click()
    element = WebDriverWait(driver, 10).until(
        # wait for the presence of a single element
        EC.presence_of_element_located((By.ID, "txtHeaderInput"))) # ()
except Exception as e:
    print(f'[Error] : {e}')
driver.find_element(by = By.ID, value = "txtHeaderInput").send_keys(keywords[0])
'''
## 3.4 css selector
# F12 - hover on the element - the Styles
# Check the css selector of the Styles
'''
driver.find_element(by = By.CSS_SELECTOR, value = '.searchAllBox>.moreBtnWrap>.moreBtn').click()
'''
## 3.5 no class & ID
# F12 - hover on the elemen - copy - css selector - delete some of css selectors 
# btn = driver.find_element(by = By.CSS_SELECTOR, value = '.pageNumBox > ul > li:nth-child(2)').click()
## 3.6 several class
# >>> https://jigeumblog.tistory.com/32
'''
.searchAllBox.overseaTravel>.boxList>li'
'''
## 3.6 Element.get_attribute()
# Click on the thumbnail - Check the web page addresses
'''
thumbnail = li.find_element(by = By.CSS_SELECTOR, value = 'img').get_attribute('src')
data_id = li.get_attribute("data-id")
print(f'Thumbnail : {thumbnail}')
print(f'Link : https://tour.interpark.com/goods/detail/?BaseGoodsCd={data_id}')
'''

## 4. Info Object 
# class TourInfo:

## 5. Beautiful Soup
# HTML, XML, DOM
# >>> https://beautiful-soup-4.readthedocs.io/en/latest/
'''
pip install bs4
'''

## 6. MariaDB
# >>> https://mariadb.com/
# 10.3.38 1234/1234 utf8
# >>> Double Click MySQL Client
# MariaDB [(none)]
'''
create database pythonDB;
''' # Query OK, 1 row affected (0.001 sec)
# >>> double Click HeidiSQL 