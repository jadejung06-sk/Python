from selenium import webdriver
import time

driver_path = "C:\Development\chromedriver.exe"
COOKIE_HTTP = "http://orteil.dashnet.org/experiments/cookie/"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(driver_path, options=options)
driver.get(COOKIE_HTTP)

buyCursor = driver.find_element_by_id("buyCursor")
buyGrandma = driver.find_element_by_id("buyGrandma")
buyFactory = driver.find_element_by_id("buyFactory")
buyMine = driver.find_element_by_id("buyMine")
buyShipment = driver.find_element_by_id("buyShipment")
buyAlchemy_lab = driver.find_element_by_id("buyAlchemy lab")
buyPortal = driver.find_element_by_id("buyPortal")
buyTime_machine = driver.find_element_by_id("buyTime machine")

cookie = driver.find_element_by_id(id_="cookie")
cookies_per_second = driver.find_element_by_id(id_="cps")
items = [buyTime_machine, buyPortal, buyAlchemy_lab, buyShipment, buyMine, buyFactory, buyGrandma, buyCursor]         

timeout = time.time() + 5
five_min = time.time() + 300

item_set = set()

while True: 
    cookie.click()
    if time.time() > timeout:
        for item in items:
            if item.get_attribute("class") == "":
                # time.sleep(5) # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
                item_set.add(item)
                # print(len(item_set), list(item_set)[-1])
                phchased_item = list(item_set)[0]
                phchased_item.click()        
        timeout = time.time() + 5
    if time.time() > five_min:
        print(cookies_per_second.text)
        driver.quit()
        break
        
