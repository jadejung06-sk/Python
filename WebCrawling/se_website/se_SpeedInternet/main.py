from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

"band Giga 라이트 : 250Mbps / band Giga : 500Mbps / band Giga 프리미엄 : 500Mbps"

PROMISED_DOWN = 500
PROMISED_UP = 350
TWITTER_EMAIL = "jungjade06@gmail.com"
TWITTER_PASSWORD = ""

class InternetSpeedTwitterBot:
    def __init__(self):
        CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)    
        # self.driver.get("https://www.speedtest.net/")
        # self.go_btn = self.driver.find_element(By.CSS_SELECTOR, "span.start-text").click()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.go_btn = self.driver.find_element(By.CSS_SELECTOR, "span.start-text").click()
        time.sleep(60)
        try:
            self.close_btn = self.driver.find_element(By.CSS_SELECTOR, "svg.svg-icon").click()
        except:
            time.sleep(180)
            print("except")
            self.close_btn = self.driver.find_element(By.CSS_SELECTOR, "svg.svg-icon").click()
        finally:
            time.sleep(180)
            self.speed_download = self.driver.find_element(By.CSS_SELECTOR, "span.result-data-large.number.result-data-value.download-speed")
            self.speed_upload = self.driver.find_element(By.CSS_SELECTOR, "span.result-data-large.number.result-data-value.upload-speed")
            print(f"Speed of Downloading: {self.speed_download.text}\nSpeed of Uploading: {self.speed_upload.text}")
    
    def tweet_at_provider(self):
        print("tweet")
        pass

if __name__ == "__main__":
    twitter = InternetSpeedTwitterBot()
    twitter.get_internet_speed()
    twitter.tweet_at_provider()





