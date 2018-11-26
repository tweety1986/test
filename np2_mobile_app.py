import os
import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ComplexAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            '../../../sample-code/apps/np2/np2.apk'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def test_tap(self):
            el = self.driver.find_element_by_accessibility_id('//android.widget.TextView')
            actions = TouchAction(self.driver)
            actions.tap(element)
            actions.perform()


    # scroll
    def test_scroll(self):
        sleep(10)
        els = self.driver.find_elements_by_xpath('//android.widget.TextView')
        self.driver.scroll(els[8], els[0])

    '''# co to daje?
    def test_find_multiple_elements(self):
        sleep(8)
        els = self.driver.find_elements_by_accessibility_id('Animation')
        self.assertIsInstance(els, list)# bez tego tez dziala

    # ???
    def test_finger_print(self):
        sleep(6)
        result = self.driver.finger_print(1)
        self.assertEqual(None, result)# bez tego tez dziala

    # ???
    def test_get_network_connection(self):
        sleep(4)
        nc = self.driver.network_connection
        self.assertIsInstance(nc, int) # bez tego tez dziala








   # close
    def tearDown(self):
        self.driver.quit()'''



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ComplexAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
