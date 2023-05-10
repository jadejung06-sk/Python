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
