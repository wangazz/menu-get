from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

# authentication
username = 'some3985'
password = ''

# driver = webdriver.Firefox()
driver = webdriver.PhantomJS('phantomjs.exe')

# enter credentials into Shibboleth identity provider
driver.get('https://meals.some.ox.ac.uk/index.php')
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_name('Submit').submit()
driver.find_element_by_class_name('go_button').click()

# go to menu page
driver.get('https://meals.some.ox.ac.uk/pallmenu.php')
driver.save_screenshot('screenshot.png')

soup = BeautifulSoup(driver.page_source, 'html.parser')

df = pd.read_html(driver.page_source)[0]