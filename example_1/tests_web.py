from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    # nie dziala cos!
    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element_by_class_name("btn btn-primary agree").click()