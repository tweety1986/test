import unittest
from selenium import webdriver


class PythonOrgSearch(unittest.TestCase):
    def test(self):

        driver = webdriver.Firefox()
        driver.get("http://www.yahoo.com")

        driver.find_element_by_css_selector('div.btn-group.clearfix.agree-button-group').click()
        driver.find_element_by_css_selector('#uh-signin').click()
        driver.find_element_by_css_selector('#login-username').click()
        driver.find_element_by_css_selector('#login-username').send_keys('Halo')
        driver.find_element_by_css_selector('#login-signin').click()
        


if __name__ == "__main__":
    unittest.main()