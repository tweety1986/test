from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Firefox
driver = webdriver.Firefox()

# ------------------------------
# The actual test scenario: Test the codepad.org code execution service.

# Go to codepad.org
driver.get('https://nowyprofil.wp.pl/rejestracja/')

driver.find_element_by_css_selector('#app > div > div > div.sc-brqgnP.dFMleh > div > div.sc-bdVaJa.dYKBpD > form > button').click()
driver.find_element_by_css_selector('#app > div > div > div.sc-brqgnP.dFMleh > div > div.sc-bdVaJa.dYKBpD > form > div.sc-bwzfXH.ViXtR > div:nth-child(1) > div > input').click()
driver.find_element_by_css_selector('#app > div > div > div.sc-brqgnP.dFMleh > div > div.sc-bdVaJa.dYKBpD > form > div.sc-bwzfXH.ViXtR > div:nth-child(1) > div > input').send_keys('Kasia')
driver.find_element_by_css_selector('div.joSNAM:nth-child(2) > div:nth-child(1) > input:nth-child(2)').click()
driver.find_element_by_css_selector('div.joSNAM:nth-child(2) > div:nth-child(1) > input:nth-child(2)').send_keys('Kowalska')
driver.find_element_by_css_selector('#app > div > div > div.sc-brqgnP.dFMleh > div > div.sc-bdVaJa.dYKBpD > form > div:nth-child(2) > div > fieldset > div > div:nth-child(1) > div > label').click()
driver.find_element_by_css_selector('#app > div > div > div.sc-brqgnP.dFMleh > div > div.sc-bdVaJa.dYKBpD > form > div:nth-child(3) > fieldset > div > div.sc-bdVaJa.puzUQ > input').click()
driver.find_element_by_css_selector('#app > div > div > div.sc-brqgnP.dFMleh > div > div.sc-bdVaJa.dYKBpD > form > div:nth-child(3) > fieldset > div > div.sc-bdVaJa.puzUQ > input').send_keys('11')
driver.find_element_by_css_selector('select.invalid').click()

select = Select(driver.find_element_by_class_name('invalid'))
select.select_by_visible_text('Maj')

driver.find_element_by_css_selector('#app > div > div > div.sc-brqgnP.dFMleh > div > div.sc-bdVaJa.dYKBpD > form > div:nth-child(3) > fieldset > div > div.sc-bdVaJa.JQfcJ > input').click()
driver.find_element_by_css_selector('#app > div > div > div.sc-brqgnP.dFMleh > div > div.sc-bdVaJa.dYKBpD > form > div:nth-child(3) > fieldset > div > div.sc-bdVaJa.JQfcJ > input').send_keys('1900')


#driver.find_element_by_css_selector('div.ng-scope:nth-child(5) > form:nth-child(2) > fieldset:nth-child(1) > button:nth-child(5)').click()
#driver.find_element_by_css_selector('div.join-link:nth-child(4) > a:nth-child(2)').click()
#driver.find_element_by_css_selector('#border-2').click()
#driver.find_element_by_css_selector('div.btn > a:nth-child(1)').click()
#driver.find_element_by_css_selector('#firstName').click()
#driver.find_element_by_css_selector('#firstName').send_keys('Jan')
#driver.find_element_by_css_selector('#lastName').click()
#driver.find_element_by_css_selector('#lastName').send_keys('Kowalski')
#driver.find_element_by_xpath('//*[@id="sexSelect"]').click()