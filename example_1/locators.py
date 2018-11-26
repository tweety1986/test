from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    # nie dziala cos!
    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element_by_class_name("btn btn-primary agree").click()

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass