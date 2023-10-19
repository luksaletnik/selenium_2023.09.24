# Install webdriver-manager: pip install webdriver-manager
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from screenshot_function import *
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com')

try:
    username_field = driver.find_element('id', 'user-name')
except NoSuchElementException:
    print('Field "user-named" not found by ID. Search by name.')
    username_field = driver.find_element('name', 'user-name')
    make_screenshot(driver)

# time.sleep(2.5)
username_field.clear()
username_field.send_keys('standard_user')

# Druga wersja:
# username_field = driver.find_element('id', 'user-name').send_keys('standard_user')

try:
    password_field = driver.find_element(By.ID, 'password')
except NoSuchElementException:
    print('Password field not found')
    driver.quit()
    raise
password_field.clear()
password_field.send_keys('secret_sauce')

login_button = driver.find_element(By.ID, 'login-button')
if not login_button.get_attribute('disabled'):
    login_button.click()
else:
    print('Login button is disabled')

time.sleep(5)

# driver.get_screenshot_as_file('screen.png')
make_screenshot(driver)

driver.quit()
