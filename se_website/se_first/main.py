from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

##### simple way
# URL = "https://www.amazon.com/Easy-Home-Ovulation-Strips-Pregnancy/dp/B00DOJG6RA/ref=sr_1_1_sspa?crid=3RJNSRNY8OPTS&keywords=pregnancy%2Btester&qid=1652195284&refinements=p_72%3A1248903011&rnid=1248901011&s=hpc&sprefix=pregnancy%2Btester%2Caps%2C224&sr=1-1-spons&smid=A2X1ZITIH00L9R&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFPOEM0RlRLME0zMEwmZW5jcnlwdGVkSWQ9QTAxOTM3NTBZUldWTTMzSTExMFcmZW5jcnlwdGVkQWRJZD1BMDA0Mjc5MDNCM1k1MFlHMUNIUjAmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1"
# driver.get(url=URL)
# css_selector= "#corePrice_desktop > div > table > tbody > tr > td.a-span12 > span.a-price.a-text-price.a-size-medium.apexPriceToPay"
# price = driver.find_element_by_css_selector(css_selector=css_selector)
# price = driver.find_element(by=By.CSS_SELECTOR, value=css_selector)
# print(price.text)
#########################

##### find an element
# URL = "https://www.python.org/"
# driver.get(url=URL)
# search_bar = driver.find_element_by_name(name ="q")
# # print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)
# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)
##############################

##### find elements
URL = "https://www.python.org/"
driver.get(url=URL)
upcoming_events = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
# print(upcoming_events)
time_list = []
name_list = []
upcoming_dict = {}
for upncoming_event in upcoming_events:
    upcoming_list = upncoming_event.text.split('\n')
    # print(upcoming_list)
    for idx, upcoming in enumerate(upcoming_list):
        if idx % 2 == 0:
            time_list.append(upcoming)
        else:
            name_list.append(upcoming)
for idx in range(len(time_list)):
    upcoming_dict[idx] = {
    "time" : time_list[idx],
    "name" : name_list[idx]
    }
print(upcoming_dict)
driver.quit() 

'''
##### an example
# Dict['Dict1'] = {}
# # Adding elements one at a time
# Dict['Dict1']['name'] = 'Bob'
# Dict['Dict1']['age'] = 21
{0 : {'time': '2020-08-28', 'name': 'Django Girls Malabo' }
1 : ~~
}
'''