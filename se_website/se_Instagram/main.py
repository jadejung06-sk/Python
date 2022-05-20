from gettext import install
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

INS_URL = "https://www.instagram.com/"
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "https://www.instagram.com/chefsteps/"
USERNAME = "j-j-s07@hanmail.net"
PASSWORD = input("Type your password:")

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
        self.facebook_id.send_keys(USERNAME) # pass
        self.facebook_pw = self.driver.find_element(By.NAME, 'pass')
        self.facebook_pw.send_keys(PASSWORD)
        self.facebook_login = self.driver.find_element(By.NAME, 'login')
        self.facebook_login.click()
        time.sleep(10)
        # try:
        #     self.alarm_btn = self.driver.find_element(By.CLASS_NAME, 'button.aOOlW.HoLwm')
        #     self.alarm_btn.click()
        # except NoSuchElementException:
        #     print("There is no element.")
        #     time.sleep(5)
        # finally:
        #     print("Final trial")
        #     self.alarm_btn = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
        #     self.alarm_btn.click()     
        
    def find_followers(self):
        time.sleep(5)
        self.driver.get(SIMILAR_ACCOUNT)

        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            #In this case we're executing some Javascript, that's what the execute_script() method does. 
            #The method can accept the script as well as a HTML element. 
            #The modal in this case, becomes the arguments[0] in the script.
            #Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        time.sleep(5)
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except :
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

# 'li.wo9IH'
# 'div._7UhW9.xLCgt.qyrsm.uL8Hv.T0kll'
# 'button.sqdOP.L3NKy.y3zKF'     
    # #find the followers window
    # dialog = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]')
    # #find number of followers
    # allfoll=int(driver.find_element_by_xpath("//li[2]/a/span").text) 
    # #scroll down the page
    # for i in range(int(allfoll/2)):
    #     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
    #     time.sleep(random.randint(500,1000)/1000)
    #     print("Extracting friends %",round((i/(allfoll/2)*100),2),"from","%100")

if __name__=="__main__":
    instagram = InstaFollower(CHROME_DRIVER_PATH)
    instagram.login()
    instagram.find_followers()
    instagram.follow()

