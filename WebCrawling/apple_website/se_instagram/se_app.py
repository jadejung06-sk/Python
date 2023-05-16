from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./WebCrawling/apple_website/se_instagram/chromedriver.exe')
driver.get('https://instagram.com')

time.sleep(3)
# e = driver.find_element_by_css_selector('div ._aa4u').text
# print(e)

##### Instgram
