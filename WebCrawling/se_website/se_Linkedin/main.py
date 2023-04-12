from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('C:\Development\chromedriver.exe', options=options)
LINK_HTTP = "https://www.linkedin.com/"
driver.get(LINK_HTTP)

##### sign form
sign_form = driver.find_elements(By.CLASS_NAME, 'sign-in-form__form-input-container input')
sign_form[0].send_keys("jungjade06@gmail.com")
pw = input("Type your password:")
sign_form[1].send_keys(pw)
sign_form[1].send_keys(Keys.ENTER)
#########################
time.sleep(5)
##### search 
# search_bar = driver.find_element_by_link_text("Search")
# search_bar = driver.find_element(By.CLASS_NAME, 'search-global-typeahead__input always-show-placeholder')
# print(search_bar)
# search_bar.send_keys("data engineer")
# search_bar.send_keys(Keys.ENTER)

# google = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/div[1]/form/button/span')
# time.sleep(2)
# google.click()
# driver.switch_to.window(driver.window_handles[1])
# # print("1",new_tap)
# time.sleep(2)
# input_box = driver.find_element(By.CLASS_NAME, "Xb9hP")
# print("2",input_box)
# time.sleep(2)
# input_box.send_keys("jungjade06@gmail.com")
# print("3", input_box)
# next_btn = driver.find_element(By.CSS_SELECTOR,"div.VfPpkd-RLmnJb")
# print("4", next_btn)

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get(LINK_HTTP)


# print(google_login.text)
# google_login.send_keys(Keys.ENTER)