from selenium import webdriver
# from bs4 import BeautifulSoup
import pandas as pd

# authentication
username = 'some3985'
password = ''

# driver = webdriver.Firefox()
driver = webdriver.PhantomJS('phantomjs.exe')

# enter credentials into Shibboleth identity provider
try:
    driver.get('https://meals.some.ox.ac.uk/index.php')
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_name('Submit').submit()
    driver.find_element_by_class_name('go_button').click()

    # go to menu page
    driver.get('https://meals.some.ox.ac.uk/pallmenu.php')

except Exception as e:
    driver.save_screenshot('screenshot.png')

# soup = BeautifulSoup(driver.page_source, 'html.parser')

df = pd.read_html(driver.page_source)[0]

meal = {
    'lunch' : 1, 
    'lunch_v' : 2, 
    'dinner' : 3, 
    'dinner_v' : 4
}

day = {
    'sun' : 2,
    'mon' : 3,
    'tue' : 4,
    'wed' : 5,
    'thu' : 6,
    'fri' : 7,
    'sat' : 8
}

# meals should be called in the form df[meal][day]
# example
df[meal['dinner']][day['thu']]