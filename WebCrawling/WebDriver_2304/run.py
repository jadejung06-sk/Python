##### Typing and Searching InterPark Tour site
## 1. Login 
# PC web Site or Mobile
## 2. pip install selenium
# pip install pymysql
# pip install bs4

from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
import pymysql as my
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from tour import TourInfo

## 3. Load driver
# Option : no images, control agent, proxy
# Check temporary files of driver capacity
PATH = './WebCrawling/WebDriver_2304/chromedriver.exe'
MAIN_URL = 'http://tour.interpark.com/'  # + slash
keywords = ['로마']
# Tour info Object list
tour_list = []

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
# Start 1 Last 5 but Test 6 (OK)
for page in range(1, 2): #range(1, 6):
    try:
        btn = driver.find_element(by = By.CSS_SELECTOR, value = f'.pageNumBox > ul > li:nth-child({page})').click()
## 7. Wait minutes
        time.sleep(2)
## 8. Get some information
# Several sites
# Name, Thumbnail, comment, range1, range2, price, review, link 
# Class
        boxItems = driver.find_elements(by = By.CSS_SELECTOR, value = '.searchAllBox.overseaTravel>.boxList>li')
        for li in boxItems:
            title = li.find_element(by = By.CSS_SELECTOR, value = 'h5.infoTitle').text
            thumbnail = li.find_element(by = By.CSS_SELECTOR, value = 'img').get_attribute('src')
            data_id = li.get_attribute("data-id")
            comment = li.find_element(by = By.CSS_SELECTOR, value = 'p.infoSubTitle').text
            price = li.find_element(by = By.CSS_SELECTOR, value = 'strong').text
            link = f'https://tour.interpark.com/goods/detail/?BaseGoodsCd={data_id}'
            print(f"Title : {title}")
            print(f'Thumbnail : {thumbnail}')
            print(f'Link : {link}')
            print(f"Sub Title : {comment}")
            print(f"Price : {price} won")
            for info in li.find_elements(by = By.CSS_SELECTOR, value = 'p.info'):
                print(f'{info.text}')
            print('=' * 100)
            # Put info. of tour in tour list title, price, area, link, img):
            obj = TourInfo(title = title, price = price, area = li.find_elements(by = By.CSS_SELECTOR, value = 'p.info')[1].text, link = link, img = thumbnail )
            tour_list.append(obj)
        print(f'Move on {page} Page')
    except Exception as e1:
        print(f'[Error] : NextPage >>> {e1}')
    # print(tour_list, len(tour_list))
    for tour in tour_list:
        # print(type(tour))
        driver.get(tour.link)
        time.sleep(1)
## 9. beautifulsoup DOM on current page
        soup = bs(driver.page_source, 'html.parser')
        data = soup.select('.tip-cover')
        print(type(data), len(data)) # <class 'bs4.element.ResultSet'>
## 10. DB


## 11. close - page / quit - driver / exit - process
driver.close()
driver.quit()
import sys
sys.exit()