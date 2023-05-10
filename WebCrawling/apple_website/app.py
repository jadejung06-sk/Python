import requests
from bs4 import BeautifulSoup
import urllib.request 


##### DATA 1
data = requests.get(url = 'https://finance.naver.com/item/sise.nhn?code=005930' ) # all data of this website
'''
print(data) # success or fail
print(data.status_code) # the number of success or fail
print(data.content) # all html data
'''
soup = BeautifulSoup(data.content, 'html.parser')
print(soup.find_all('strong', id = "_nowVal")[0].text) # input : tag name, id # output : list
print(soup.find_all('span', class_ = 'tah')[5].text)
'''
print(soup) # more visible and all html data
'''

##### IMAGES
img = soup.select('#img_chart_area')[0]
urllib.request.urlretrieve(soup.select('#img_chart_area')[0]['src'], './WebCrawling/apple_website/img.jpg')
'''
print(img)
print(img['src'])

'''

###### DATA 2
data = requests.get(url = 'https://finance.naver.com/item/sise.nhn?code=005930' ) 
soup = BeautifulSoup(data.content, 'html.parser')
print(soup.find_all('strong', id = "_nowVal")[0].text) # input : tag name, id # output : list
print(soup.find_all('span', class_ = 'tah')[5].text)
