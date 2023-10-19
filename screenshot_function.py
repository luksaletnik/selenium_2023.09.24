import datetime

def make_screenshot(driver):
    today = datetime.datetime.today()
    short_date = today.strftime('_stamp%H%M%S')
    screen_name = 'C:\\Users\\luksa\\PycharmProjects\\selenium_2023.09.24\\saucedemo_screenshot\\' + 'screen' + short_date + '.png'
    driver.get_screenshot_as_file(screen_name)