##### Typing and Searching InterPark Tour site
## 1. Login 
# PC web Site or Mobile
## 2. pip install selenium
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

## 3. Load driver
# Option : no images, control agent, proxy
# Check temporary files of driver capacity
PATH = './WebCrawling/WebDriver_2304/chromedriver.exe'
MAIN_URL = 'http://tour.interpark.com/'  # + slash
keywords = ['로마']
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(options=options, executable_path=PATH)
# driver = wd.Chrome(PATH)
## 4. Connect on Site
driver.get(MAIN_URL)
## 5. Point Searching Button and Typing some words
# ID > Class > Paraent > Sibbling
# ID divHeaderSearch
# element or elements
try:
    driver.find_element(by = By.ID, value = "divHeaderSearch").click()
    element = WebDriverWait(driver, 10).until(
        # wait for the presence of a single element
        EC.presence_of_element_located((By.ID, "txtHeaderInput"))) # ()
except Exception as e:
    print(f'[Error] : divHeaderSearch >>> {e}')
driver.find_element(by = By.ID, value = "txtHeaderInput").send_keys(keywords[0])

try:
    driver.find_element(by = By.ID, value = "btnHeaderInput").click()
except Exception as e:
    print(f'[Error] : btnHeaderInput >>> {e}')
driver.find_element(by = By.CSS_SELECTOR, value = '.searchAllBox>.moreBtnWrap>.moreBtn').click()
## 6. Click on searching button
for i in range(1, 6):
    btn = driver.find_element(by = By.CSS_SELECTOR, value = f'.pageNumBox > ul > li:nth-child({i})').click()
## 7. Wait minutes

## 8. Get some information