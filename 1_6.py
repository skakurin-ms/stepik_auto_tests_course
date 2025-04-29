#task 1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
from time import sleep
from typing import final

#task 2
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# URL = "http://suninjuly.github.io/find_link_text"
# formula = str(math.ceil(math.pow(math.pi, math.e)*10000))
# browser = webdriver.Chrome()
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(URL)
#     link = browser.find_element(By.LINK_TEXT, f"{formula}")
#     link.click()
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(5)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


#task #3
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# URL = "http://suninjuly.github.io/huge_form.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(URL)
#
#     sleep(3)
#
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     for element in elements:
#         element.send_keys("Text123")
#
#     submit_button = browser.find_element(By.CLASS_NAME, "btn")
#     submit_button.click()
#
#     sleep(10)
# finally:
#     browser.quit()


#task 4
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.XPATH, "//button[@type='submit']")
#     button.click()
#
#     sleep(5)
# finally:
#     browser.quit()


#task 5

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    sleep(5)
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class .first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class .second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class .third")
    input3.send_keys("ivan_petrov@gmail.com")

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

    sleep(5)
finally:
    browser.quit()