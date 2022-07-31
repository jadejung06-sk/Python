from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

TINDER_HTTP = "https://tinder.com/"
driver = webdriver.Chrome("C:\Development\chromedriver")
driver.get(TINDER_HTTP)

time.sleep(5)
login = driver.find_element(By.XPATH, '//*[@id="q1028785088"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
login.click()

time.sleep(5)
facebook_login = driver.find_element(By.XPATH, '//*[@id="q-699595988"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
facebook_login.click()

time.sleep(5)
driver.switch_to.window(driver.window_handles[-1])
facebook_id = driver.find_element(By.ID, "email")
facebook_id.send_keys("j-j-s07@hanmail.net")
facebook_pw = driver.find_element(By.ID, "pass")
pw = input("Type your password:")
facebook_pw.send_keys(pw)

facebok_btn = driver.find_element(By.ID, "loginbutton")
facebok_btn.click()

time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
agree_btn = driver.find_element(By.XPATH, '//*[@id="q-699595988"]/div/div/div/div/div[3]/button[1]/span')
agree_btn.click()

time.sleep(5)
alarm_btn = driver.find_element(By.XPATH, '//*[@id="q-699595988"]/div/div/div/div/div[3]/button[2]/span')
alarm_btn.click()

time.sleep(5)
cookie_btn = driver.find_element(By.XPATH, '//*[@id="q1028785088"]/div/div[2]/div/div/div[1]/div[1]/button/span')
cookie_btn.click()

for n in range(50):
    
    time.sleep(1)
    try:
        print("called")
        like_btn = driver.find_element(By.XPATH, '//*[@id="q1028785088"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button/span/span')
        like_btn.click() 
    except:
        time.sleep(5)

driver.quit()
