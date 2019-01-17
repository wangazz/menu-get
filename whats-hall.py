from selenium import webdriver
import pandas as pd

# authentication
username = 'some3985'
password = input("Password? ")

# driver = webdriver.Firefox()
driver = webdriver.PhantomJS('phantomjs.exe')
driver.set_window_size(1000,500)

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

df = pd.read_html(driver.page_source)[0]

meal = {
    'lun' : 1, 
    'lun_v' : 2, 
    'din' : 3, 
    'din_v' : 4
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
print(df[meal['lun']][day['wed']])