##### pip install
# requests connect website
# bs4 web analysis
'''
pip install requests
pip install bs4
'''

##### Inspection on the website
# hover on the data
# id : unique tag
# class_ : one or more things (2 ea. +)
'''
<strong class="tah p11" id="_nowVal">
soup.find_all('strong', id = "_nowVal")
soup.find_all('strong', id = "_nowVal")[0]
soup.find_all('strong', id = "_nowVal")[0].text

<span class="tah p11" id="_quant">
soup.find_all('span', class_ = "tah") # input : one of them output :  100 ea.
soup.find_all('span', class_ = 'tah')[0]
soup.find_all('span', class_ = 'tah')[1]
soup.find_all('span', class_ = 'tah')[2]
soup.find_all('span', class_ = 'tah')[#]
soup.find_all('span', class_ = 'tah')[5].text
'''

##### separate words
## em upper class
'''
soup.find_all('em', class_='no_down').text
'''

##### no id, no class
## em tag
## select() 
# tag
# class == . 
# id == #
# inner attribute ' '
'''
soup.find_all('em')[#].text
soup.select('.f_down') # css selector
soup.select('strong#_nowVal')
soup.select('.gray .f_down em')[0].text # inner attribute
'''

##### images
## <img>
# download urllib.request.urlretrieve
'''
soup.select('#img_chart_area')[0]
soup.select('#img_chart_area')[0]['src']
import urllib.request 
urllib.request.urlretrieve(soup.select('#img_chart_area')[0]['src'], 'img.jpg')
'''

##### unlimited scroll (ajax)
## pages
'''
requests.get('pageurl?page=1')
requests.get('pageurl?page=2')
requests.get('pageurl?page=3')
'''
## no pages
# demerit = get only first content
# have to get more contents
# Network tap > file Name > Search : short words of title > Headers tap
'''
a = request.get('https://s.search.naver.com/p/review/search.naver? ... )
'''
##### back slash (escape)
'''
data= request.get('https://s.search.naver.com/p/review/search.naver? ... )
soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser')
txt_list = soup.select('a.api_txt_lines')
print(txt_list[0].text)
print(txt_list[0]['href'])
'''
##### query
## korean without encoding
'''
data = requests.get(https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%82%AC%EA%B3%BC)
data = requests.get(https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=사과)
'''

##### data in chart
## search the html file
# Network > Headers or Preview
# ' ' dic vs. " " json
# make a json file and change it in format document
## check what thml files are added
# Network > Headers
'''
import json
data = requests.get()
dict_data = json.loads(data.content)
dict_data['data'][0]['Close']
dict_data['data'][1]['Close']
dict_data['data'][2]['Close']
'''

##### Datetime
# epoch time 10 19700101~
# unix time 10
# 3 miliseconds
'''
import json
import time
data = requests.get()
dict_data = json.loads(data.content)
dict_data['data'][0]['DT']
time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1610175600000/1000)) # 13 to 10
time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(dict_data['data'][0]['DT'])/1000)) # 13 to 10
'''

##### Multi (No Class version)
## multi-processing
# more python cmds
# a processer locks a variable
'''
from multiprocessing import Pool # Processors
'''
## multi-threading
# more cpu threads
'''
from multiprocessing.dummy import Pool as ThreadPool # Threads
pool = ThreadPool(4) # num of threads
pool.map(func, list) # work the tasks
pool.close() # stop pooling
pool.join() # wait for the result (list)
'''
## map()
# work the same task for each in a list
'''
def func return i +1
map(func, list)
'''

##### 4xx 5xx status code
## Network >> f5 + the first file >> Request Headers
# User-Agent
# cookie " to '
# Application >> Storage >> Cookies

'''
User-Agent
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36
cookie
regStatus=pre-register; session-id=136-0386987-0320005; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:KR"; skin=noskin; ubid-main=132-4186484-1617212; session-token="NyQVTb3oX9HkScNoPv673JmuVqg4S4G0nr5vEDrujgR+jCSx8lX5oxqKG+DMdnBVNBzLMQBS7Q30KK0nXtCNefseSH/uAy5bLyKg7J3+urDAafHDXzkIi5j0yJ5akwq7pz2rEhGotbnKHIExlJQtAC/MspTJke2IU82pR0BIl8Davowv8s63mQQmLmSlKdYKSXGp57O2SF42UFGepK3Kp8VODm2bsT4W3db5o+a+Tjc="; csm-hit=tb:s-ENRPD2CMT9T17RC894AW|1684321801143&t:1684321801899&adb:adblk_no
'''

'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}
cookies = {
'regStatus': 'pre-register',
'session-id': '136-0386987-0320005',
'session-id-time': '2082787201l',
'i18n-prefs': 'USD',
'sp-cdn': 'L5Z9:KR',
'skin': 'noskin',
'ubid-main': '132-4186484-1617212',
'session-token': 'NyQVTb3oX9HkScNoPv673JmuVqg4S4G0nr5vEDrujgR+jCSx8lX5oxqKG+DMdnBVNBzLMQBS7Q30KK0nXtCNefseSH/uAy5bLyKg7J3+urDAafHDXzkIi5j0yJ5akwq7pz2rEhGotbnKHIExlJQtAC/MspTJke2IU82pR0BIl8Davowv8s63mQQmLmSlKdYKSXGp57O2SF42UFGepK3Kp8VODm2bsT4W3db5o+a+Tjc=',
'csm-hit': 'tb:s-ENRPD2CMT9T17RC894AW|1684321801143&t:1684321801899&adb:adblk_no'
}
amazon_get = requests.get('https://www.amazon.com/s?k=monitor&crid=2VB5OZLFE2M4T&sprefix=monit%2Caps%2C330&ref=nb_sb_noss_2', headers=headers, cookies=cookies)
'''