import unittest
from selenium import webdriver


class OnetSearch(unittest.TestCase):
    def test(self):

        driver = webdriver.Firefox()
        driver.get("http://www.onet.pl")

        driver.find_element_by_css_selector('#tabMenu > div > ul > li:nth-child(1)').click()
        #driver.find_element_by_css_selector('button.cmp-button_button:nth-child(2)').click()
        #driver.find_element_by_css_selector('#tabMenu > div > ul > li:nth-child(2)').click()
        #driver.find_element_by_css_selector('#login-username').send_keys('kocham Cie')
        #driver.find_element_by_css_selector('#login-signin').click()


if __name__ == "__main__":
    unittest.main()