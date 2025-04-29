#task 1
from time import sleep
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
#
# URL = "http://suninjuly.github.io/alert_accept.html"
#
# def calc(x):
#    return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(URL)
#     sleep(1)
#
#     submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
#     submit_button.click()
#
#     alert = browser.switch_to.alert
#     alert.accept()
#
#     x = browser.find_element(By.ID, "input_value").text
#     calculation = calc(x)
#
#     result_field = browser.find_element(By.ID, "answer")
#     result_field.send_keys(calculation)
#
#     submit_button2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
#     submit_button2.click()
#     sleep(4)
#
# finally:
#     browser.quit()

#task 2
URL = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(URL)
    sleep(2)

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, "input_value").text
    calculation = calc(x)

    result_field = browser.find_element(By.ID, "answer")
    result_field.send_keys(calculation)

    submit_button2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button2.click()
    sleep(4)

finally:
    browser.quit()
