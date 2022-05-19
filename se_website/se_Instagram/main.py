from gettext import install
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

INS_URL = "https://www.instagram.com/"
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = ""
PASSWORD = ""

class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(path)
        self.driver.get(INS_URL)

    def login(self):
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, 'span.KPnG0').click()
        print("login")
        time.sleep(5)
        self.facebook_id = self.driver.find_element(By.NAME, 'email')
        self.facebook_id.send_keys("j-j-s07@hanmail.net") # pass
        self.facebook_pw = self.driver.find_element(By.NAME, 'pass')
        self.facebook_pw.send_keys(input("Type your password:"))
        self.facebook_login = self.driver.find_element(By.NAME, 'login')
        self.facebook_login.click()
        time.sleep(5)

    def find_followers(self):
        print("find")
        pass

    def follow(self):
        print("follow")
        pass

if __name__=="__main__":
    instagram = InstaFollower(CHROME_DRIVER_PATH)
    instagram.login()
    instagram.find_followers()
    instagram.follow()

