import requests
from bs4 import BeautifulSoup

# '''
# Accept-Language:
# ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7

# User-Agent:
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36
# '''

headers = {'Accept-Language' : "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"}
ITEM_HTTP = r"https://www.amazon.com/Easy-Home-Ovulation-Strips-Pregnancy/dp/B00DOJG6RA/ref=sr_1_1_sspa?crid=3RJNSRNY8OPTS&keywords=pregnancy%2Btester&qid=1652195284&refinements=p_72%3A1248903011&rnid=1248901011&s=hpc&sprefix=pregnancy%2Btester%2Caps%2C224&sr=1-1-spons&smid=A2X1ZITIH00L9R&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFPOEM0RlRLME0zMEwmZW5jcnlwdGVkSWQ9QTAxOTM3NTBZUldWTTMzSTExMFcmZW5jcnlwdGVkQWRJZD1BMDA0Mjc5MDNCM1k1MFlHMUNIUjAmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1"
# print(ITEM_HTTP)
response = requests.get(url = ITEM_HTTP, headers=headers)
body = response.text

soup = BeautifulSoup(markup=body, "html.parser")
soup.select(selector="span.a-price.a-text-price.a-size-medium")