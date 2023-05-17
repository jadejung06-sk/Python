import requests
from bs4 import BeautifulSoup


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
# print(amazon_get.content)
# print(amazon_get.status_code)

soup = BeautifulSoup(amazon_get.content, 'html.parser')
print(soup.select('.a-size-medium'))