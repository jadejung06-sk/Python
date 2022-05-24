import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import time

headers = {'Accept-Language' : "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"}

ESTATE_URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.52063759862965%2C%22east%22%3A-122.04753884374684%2C%22south%22%3A37.50357102822873%2C%22north%22%3A37.93916175844443%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
SURVEY_URL = 'https://forms.gle/ZzVpR1zaMakt6LEU8'


response = requests.get(ESTATE_URL, headers=headers)
print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")

link_list = []
price_list = []
address_list = []
##### Links
links = soup.find_all("a", attrs={"class", 'list-card-link list-card-link-top-margin list-card-img'})
len_links = len(links)
for link in links:
    link = link.get('href')
    link_list.append(link)
    
##### Prices
prices = soup.find_all("div", attrs={"class":"list-card-price"})
for price in prices[:len_links]:
    price = price.text
    regex = re.compile("^\$\d\,\d+")
    price = regex.findall(price)[0]
    price_list.append(price)
    # real_state_info["price"].append(price)

##### Addresses
addresses = soup.find_all("address", attrs={"class":"list-card-addr"})
for addresss in addresses[:len_links]:
    address = addresss.text
    address_list.append(address)
    # real_state_info["address"].append(address)
# print(link_list, price_list, address_list)

##### dict
real_state_info = { "link": link_list,
"price":price_list,
"address": address_list}
# print(real_state_info)

##### selenium

chrome_driver_path = Service("C:\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get(SURVEY_URL)
time.sleep(2)
# answer_box = driver.find_element(By.CLASS_NAME, 'Hvn9fb.zHQkBf')
# print(answer_box)

