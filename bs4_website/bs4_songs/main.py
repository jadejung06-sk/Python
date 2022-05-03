import requests
from bs4 import BeautifulSoup
import datetime


time = input("Which year do you want to travel to? Type the date in this format like 20000812:")
THETIME = datetime.datetime.strptime(time, "%Y%m%d").date()
# THETIME = "2000-08-12"
# print(THETIME)

URL = f"https://www.billboard.com/charts/hot-100/{THETIME}/"
response = requests.get(URL)
HTML = response.text

soup = BeautifulSoup(HTML, "parser.html")
soup.find()


### examples
''' h3 id="title-of-a-story" class="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 ~~
title 1 
<h3 id="title-of-a-story" class="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet">
Incomplete</h3>

title 2
<h3 id="title-of-a-story" class="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only">
Bent		
</h3>
''' 

'''
singer 1 span class="c-label a-no-truncate a-font-primary-s ~~
<span class="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet">
Sisqo
</span>

singer 2
<span class="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only">
matchbox twenty
</span>

'''

