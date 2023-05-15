##### Install chromedriver
## web address window
'''chrome://version'''
# >>> 109.0.5414.141 (공식 빌드) (64비트) (cohort: Windows 8 & 8.1)  
# download > copy and paste the webdriver file

##### pip install
## more conviniet than requests and bs4
## ajax websites
## need to login
'''pip install selenium'''

##### driver
## driver gets all data including images and texts on this web page.
'''
driver.find_element_by_css_selector('input[name="username"]').text
driver.find_element_by_css_selector('#id_name').text
driver.find_element_by_css_selector('.class_name').text
'''

##### css selector
## narrow and single css