from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = "https://www.amazon.com/Easy-Home-Ovulation-Strips-Pregnancy/dp/B00DOJG6RA/ref=sr_1_1_sspa?crid=3RJNSRNY8OPTS&keywords=pregnancy%2Btester&qid=1652195284&refinements=p_72%3A1248903011&rnid=1248901011&s=hpc&sprefix=pregnancy%2Btester%2Caps%2C224&sr=1-1-spons&smid=A2X1ZITIH00L9R&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFPOEM0RlRLME0zMEwmZW5jcnlwdGVkSWQ9QTAxOTM3NTBZUldWTTMzSTExMFcmZW5jcnlwdGVkQWRJZD1BMDA0Mjc5MDNCM1k1MFlHMUNIUjAmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1"

driver.get(url=URL)
# price = driver.find_element_by_id(id_="priceblock_ourpirce")
css_selector= "#corePrice_desktop > div > table > tbody > tr > td.a-span12 > span.a-price.a-text-price.a-size-medium.apexPriceToPay"
price = driver.find_element_by_css_selector(css_selector=css_selector)
# price = driver. find_element(by=By.CSS_SELECTOR, value=css_selector)
print(price.text)

driver.quit() 