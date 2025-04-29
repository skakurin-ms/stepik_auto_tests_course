# #task 1
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# URL = "https://suninjuly.github.io/selects1.html"
#
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(URL)
#     sleep(2)
#
#     num1 = browser.find_element(By.ID, "num1").text
#     num2 = browser.find_element(By.ID, "num2").text
#     sum_ = int(num1) + int(num2)
#
#     browser.find_element(By.ID, "dropdown").click()
#     browser.find_element(By.CSS_SELECTOR, f"[value='{sum_}']").click()
#
#     submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
#     submit_button.click()
#     sleep(4)
# finally:
#     browser.quit()

#task 2

# import math
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# URL = "https://SunInJuly.github.io/execute_script.html"
#
# def calc(x):
#    return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(URL)
#     sleep(2)
#
#     x = browser.find_element(By.ID, "input_value").text
#     calculation = calc(x)
#     answer_field = browser.find_element(By.ID, "answer")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", answer_field)
#     answer_field.send_keys(calculation)
#
#     robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
#     robot_checkbox.click()
#
#     robot_radio_button = browser.find_element(By.ID, "robotsRule")
#     robot_radio_button.click()
#
#     button = browser.find_element(By.TAG_NAME, "button")
#     button.click()
#     sleep(5)
# finally:
#     browser.quit()

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

URL = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(URL)
    sleep(1)

    name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    name.send_keys("Ivan")
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("ivan_petrov@gmail.com")


    path = os.getcwd() + "/" +  "selenium_unit_2.txt"
    print(path)

    file_upload = browser.find_element(By.ID, "file")
    file_upload.send_keys(path)


    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    sleep(4)

finally:
    browser.quit()