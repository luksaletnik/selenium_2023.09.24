from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from screenshot_function import *
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com')

username_field = driver.find_element('id', 'user-name')
username_field.send_keys('standard_user')

# Druga wersja:
# username_field = driver.find_element('id', 'user-name').send_keys('standard_user')

password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('secret_sauce')

login_button = driver.find_element('id', 'login-button')
login_button.click()

time.sleep(5)

# driver.get_screenshot_as_file('screen.png')
make_screenshot(driver)

driver.quit()
