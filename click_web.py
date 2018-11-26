from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.yahoo.com")

driver.find_element_by_css_selector('div.btn-group.clearfix.agree-button-group').click()
driver.find_element_by_css_selector('#uh-signin').click()
driver.find_element_by_css_selector('#login-username').click()
driver.find_element_by_css_selector('#login-username').send_keys('kocham Cie')
driver.find_element_by_css_selector('#login-signin').click()

