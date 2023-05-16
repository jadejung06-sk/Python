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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import sys
import time
import urllib.request

sys.path.append('D:\\2022\\Python') # Only need
# print(sys.path)
from gitignore.personal import Personal
#########################
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome('./WebCrawling/apple_website/se_instagram/chromedriver.exe', options=chrome_options)
###### Login
personal = Personal()
# ID, PW = personal._get_info('instagram')
ID, PW = personal._get_info('facebook')
# driver.get('https://instagram.com')
driver.get('https://www.instagram.com/explore/tags/%EC%82%AC%EA%B3%BC/')
time.sleep(2)
search_apple = driver.find_element(by=By.CSS_SELECTOR, value= '._aagw').click()
time.sleep(2)
facebook_click = driver.find_element(by=By.CSS_SELECTOR, value= '._ab37').click()
time.sleep(5)
id_input = driver.find_element(by=By.CLASS_NAME, value= 'clearfix #email')
id_input.send_keys(ID)
time.sleep(2)
pw_input = driver.find_element(by=By.CLASS_NAME, value='clearfix #pass')
pw_input.send_keys(PW)
time.sleep(2)
pw_input.send_keys(Keys.ENTER)
driver.implicitly_wait(10)
search_apple = driver.find_element(by=By.CSS_SELECTOR, value= '._aagw').click()

##### Images '._aao_ ._aagu ._aagv .x5yr21d'
## once or twice
# img = driver.find_element(by = By.CSS_SELECTOR, value = '._aao_ .x5yr21d').get_attribute('src')
# urllib.request.urlretrieve(img, f'./WebCrawling/apple_website/se_instagram/1.jpg')g
# time.sleep(2)
# new_page = driver.find_element(by = By.CSS_SELECTOR, value = '._aaqg ._abl-')
# driver.execute_script('arguments[0].click();', new_page )
# time.sleep(2)

# img = driver.find_element(by = By.CSS_SELECTOR, value = '._aao_ .x5yr21d').get_attribute('src')
# urllib.request.urlretrieve(img, f'./WebCrawling/apple_website/se_instagram/2.jpg')
# time.sleep(2)
# new_page = driver.find_element(by = By.CSS_SELECTOR, value = '._aaqg ._abl-')
# driver.execute_script('arguments[0].click();', new_page )
# time.sleep(2)

## for 50 times
for i in range(1, 51):
    img = driver.find_element(by = By.CSS_SELECTOR, value = '._aao_ .x5yr21d').get_attribute('src')
    urllib.request.urlretrieve(img, f'./WebCrawling/apple_website/se_instagram/{i}.jpg')
    time.sleep(2)
    new_page = driver.find_element(by = By.CSS_SELECTOR, value = '._aaqg ._abl-')
    driver.execute_script('arguments[0].click();', new_page )
    time.sleep(2)




# print(img)
# #### Instgram
# # Click the first image
# # driver.implicitly_wait(10)
# ## Move on a page
# time.sleep(3)
# # e = driver.find_element_by_css_selector('div ._aa4u').text
# # print(e)


