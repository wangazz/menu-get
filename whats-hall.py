from selenium import webdriver
from selenium.webdriver.support.ui import Select

username = 'some3985'
password = 'password'

driver = webdriver.PhantomJS('phantomjs.exe')

driver.get('https://meals.some.ox.ac.uk/pallmenu.php')
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_name('Submit').click()

driver.find_element_by_class_name('go_button').click()
element = driver.find_element_by_tag_name('table')
print(element.text)