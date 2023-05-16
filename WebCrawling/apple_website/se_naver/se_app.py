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
