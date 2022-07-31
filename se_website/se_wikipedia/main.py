from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver_path = "C:\Development\chromedriver"

driver = webdriver.Chrome(driver_path)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element_by_tag_name(name="b")
# article_count.click()

# all_portals = driver.find_element_by_link_text("Wikipedia")
# all_portals.click()

# search_bar = driver.find_element_by_css_selector("input#searchInput.vector-search-box-input")
# search_bar.send_keys("python")
# search_bar.send_keys(Keys.ENTER)


##### input some data and click a btn
App_HTTP = "http://secure-retreat-92358.herokuapp.com/"
driver.get(App_HTTP)
first_name = driver.find_element_by_css_selector("input.form-control.top")
first_name.send_keys("ok")
last_name = driver.find_element_by_css_selector("input.form-control.middle")
last_name.send_keys("jung")
email = driver.find_element_by_css_selector("input.form-control.bottom")
email.send_keys("test.01@gmail.com")
sign_up_btn = driver.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-block")
sign_up_btn.click()
