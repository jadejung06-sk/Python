##### No module Found
# print(sys.path)
['d:\\2022\\Python\\WebCrawling\\apple_website\\se_instagram', 
 'C:\\Users\\jjs06\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 
 'C:\\Users\\jjs06\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 
 'C:\\Users\\jjs06\\AppData\\Local\\Programs\\Python\\Python310\\lib', 
 'C:\\Users\\jjs06\\AppData\\Local\\Programs\\Python\\Python310', 
 'C:\\Users\\jjs06\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages', 
 'C:\\Users\\jjs06\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\win32',
 'C:\\Users\\jjs06\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\win32\\lib',
 'C:\\Users\\jjs06\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\Pythonwin']
# sys.path.append('D:\\2022\\Python\\WebCrawling\\apple_website\\se_instagram')
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
sys.path.append('D:\\2022\\Python') # Only need
# print(sys.path)
from gitignore.personal import Personal
#########################

###### Login
personal = Personal()
# ID, PW = personal._get_info('instagram')
ID, PW = personal._get_info('facebook')
driver = webdriver.Chrome('./WebCrawling/apple_website/se_instagram/chromedriver.exe')
driver.get('https://instagram.com')

time.sleep(3)
facebook_click = driver.find_element_by_css_selector('._ab37').click()
time.sleep(5)
id_input = driver.find_element_by_class_name('clearfix #email')
id_input.send_keys(ID)
time.sleep(2)
pw_input = driver.find_element_by_class_name('clearfix #pass')
pw_input.send_keys(PW)
time.sleep(2)
pw_input.send_keys(Keys.ENTER)
# e = driver.find_element_by_css_selector('div ._aa4u').text
# print(e)
#### Instgram
# Click the first image
# driver.implicitly_wait(10)
## Move on a page
driver.get('https://www.instagram.com/explore/tags/%EC%82%AC%EA%B3%BC/')
search_apple = driver.find_element_by_css_selector('._aagw')
## Next page
