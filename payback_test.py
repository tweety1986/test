import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class PaybackRegistration(unittest.TestCase):
    def test(self):
        driver = webdriver.Firefox()
        driver.get("http://www.payback.pl")

        driver.find_element_by_css_selector('#header-plain > div:nth-child(3) > a:nth-child(1)').click()
        driver.find_element_by_css_selector('div.ng-scope:nth-child(5) > form:nth-child(2) > fieldset:nth-child(1) > button:nth-child(5)').click()
        driver.find_element_by_css_selector('div.join-link:nth-child(4) > a:nth-child(2)').click()
        driver.find_element_by_css_selector('#border-4').click()
        driver.find_element_by_css_selector('div.btn > a:nth-child(1)').click()
        driver.find_element_by_css_selector('#firstName').click()
        driver.find_element_by_css_selector('#firstName').send_keys('Jan')
        driver.find_element_by_css_selector('#lastName').click()
        driver.find_element_by_css_selector('#lastName').send_keys('Kowalski')
        driver.find_element_by_xpath('//*[@id="sexSelect"]').click()
        driver.find_element_by_css_selector('#sexSelect').click()

        select = Select(driver.find_element_by_class_name('gender-input modal-container ng-scope ng-blur'))
        select.select_by_visible_text('Kobieta')









if __name__ == "__main__":
    unittest.main()


