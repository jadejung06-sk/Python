##### Install chromedriver
## web address window
'''chrome://version'''
# >>> 109.0.5414.141 (공식 빌드) (64비트) (cohort: Windows 8 & 8.1)  
# download > copy and paste the webdriver file

##### pip install
## more conviniet than requests and bs4
## ajax websites
## need to login
'''pip install selenium'''

##### No moudle
## add Upper Folder
'''
import sys
import time
sys.path.append('D:\\2022\\Python') # Only need
# print(sys.path)
from gitignore.personal import Personal
personal = Personal()
'''

##### ID / PW
## https://ddolcat.tistory.com/713
'''
pip install cryptography
from cryptography.fernet import Fernet
ID, PW = Personal()._info ...
key = Fernet.generate_key()
print(f'Key : {key}')

fernet = Fernet(key)
encrypt_str = fernet.encrypt(PW)

'''

##### driver
## driver gets all data including images and texts on this web page.
'''
driver.find_element_by_css_selector('input[name="username"]').text
driver.find_element_by_css_selector('#id_name').text
driver.find_element_by_css_selector('.class_name').text
'''

##### css selector
## narrow and single css


##### use JS
'''
e = driver.find_element_by_css_selector('._65Bje')
driver.execute_script('arguments[0].click();', e )
'''

##### driver Options
## user-data-dir
'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(r"user-data-dir=C:\Users\jjs06\AppData\Local\Google\Chrome\User Data\Default")
driver = webdriver.Chrome('./WebCrawling/apple_website/se_instagram/chromedriver.exe', chrome_options=chrome_options)
'''

##### copy and paste
'''
pip install pyperclip
pyperclip.copy(str)
'''