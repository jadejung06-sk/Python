##### Typing and Searching InterPark Tour site
## 1. Login 
# PC web Site or Mobile
## 2. pip install selenium
from selenium import webdriver as wd
## 3. Load driver
# Option : no images, control agent, proxy
# Check temporary files of driver capacity
PATH = './WebCrawling/WebDriver_2304/chromedriver.exe'
MAIN_URL = 'http://tour.interpark.com/'  # + slash
keywords = ['로마']

driver = wd.Chrome(executable_path=PATH)
## 4. Connect on Site
driver.get(MAIN_URL)
## 5. Point Searching Button and Typing some words
# ID > Class > Paraent > Sibbling
# ID divHeaderSearch
# element or elements
driver.find_element_by_id(id_ = "divHeaderSearch")#.send_keys(keywords[0])


## 6. Click on searching button

## 7. Wait minutes

## 8. Get some information