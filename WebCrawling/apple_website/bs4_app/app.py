import requests
from bs4 import BeautifulSoup
import urllib.request 


##### Method 1
def get_price(company = '005930'):
    data = requests.get(url = f'https://finance.naver.com/item/sise.nhn?code={company}' ) # all data of this website
    soup = BeautifulSoup(data.content, 'html.parser')
    price = soup.find_all('strong', id = "_nowVal")[0].text
    print(price) # input : tag name, id # output : list
    tmp = soup.find_all('span', class_ = 'tah')[5].text 
    print(tmp)
    return f'{company}: {price}'
# sam_price = get_price(company ='005930')
# lg_price = get_price(company= '066575')
# f = open("./WebCrawling/apple_website/a.txt", 'w')
# f.write(sam_price)
# f.wirte(lg_price)
# f.close()


##### Method 2
company_list = ['005930', '066575', '005380', '035720', '034220', '003490' ]
cur_price_list = []
for com in company_list:
    cur_price_list.append(get_price(com))

f = open("./WebCrawling/apple_website/a.txt", 'w')
for price in cur_price_list:
        f.write('\n' + price)
f.close()






##### DATA 1
# data = requests.get(url = 'https://finance.naver.com/item/sise.nhn?code=005930' ) # all data of this website
'''
print(data) # success or fail
print(data.status_code) # the number of success or fail
print(data.content) # all html data
'''
# soup = BeautifulSoup(data.content, 'html.parser')
# print(soup.find_all('strong', id = "_nowVal")[0].text) # input : tag name, id # output : list
# print(soup.find_all('span', class_ = 'tah')[5].text)
'''
print(soup) # more visible and all html data
'''

##### IMAGES
# img = soup.select('#img_chart_area')[0]
# urllib.request.urlretrieve(soup.select('#img_chart_area')[0]['src'], './WebCrawling/apple_website/img.jpg')
'''
print(img)
print(img['src'])

'''

###### DATA 2
# data = requests.get(url = 'https://finance.naver.com/item/sise.nhn?code=005930' ) 
# soup = BeautifulSoup(data.content, 'html.parser')
# print(soup.find_all('strong', id = "_nowVal")[0].text) # input : tag name, id # output : list
# print(soup.find_all('span', class_ = 'tah')[5].text)
