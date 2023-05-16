import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import sys
sys.path.append('D:\\2022\\Python') # Only need
import time
from gitignore.personal import Personal

##### Conf. of driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(r"user-data-dir=C:\Users\jjs06\AppData\Local\Google\Chrome\User Data\Default")
driver = webdriver.Chrome('./WebCrawling/apple_website/se_instagram/chromedriver.exe', chrome_options=chrome_options)
driver.get("https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/aside/")
time.sleep(2)


##### login
ID, PW = Personal()._get_info('naver')
pyperclip.copy(ID)
id_input = driver.find_element(by=By.CSS_SELECTOR, value = '#id')
id_input.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

pyperclip.copy(PW)
pw_input = driver.find_element(by=By.CSS_SELECTOR, value = '#pw')
pw_input.send_keys(Keys.CONTROL, 'v')
time.sleep(1)
pw_input.send_keys(Keys.ENTER)


##### move a page
time.sleep(2)
blog_click = driver.find_elements(by = By.CSS_SELECTOR, value = '.sa_mw')[2].click()
driver.get(r"https://blog.editor.naver.com/editor?deviceType=mobile&returnUrl=https%3A%2F%2Fm.blog.naver.com%2FFeedList.naver&targetCategory=21")
time.sleep(2)

title_text = driver.find_elements(by = By.CSS_SELECTOR, value = '.se_textarea')[0]
title_text.send_keys(f"{time.time()}")
print('title_text', title_text)
time.sleep(1)

content_text = driver.find_element(by = By.CSS_SELECTOR, value = '.se_editable')
content_text.send_keys(f"I am happy today, too! \n So do my family memebers!")
time.sleep(2)

upload_btn = driver.find_element(by = By.CSS_SELECTOR, value = '.btn_applyPost').click()
time.sleep(2)