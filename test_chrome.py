from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

path = "C:\\Users\lenovo\geckodriver\chromedriver.exe"
driver = Chrome (executable_path=path)
driver.get("http://www.payback.pl/witamy")




