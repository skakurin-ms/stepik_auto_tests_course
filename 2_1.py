#task 3
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import math
#
# URL = "https://suninjuly.github.io/math.html"
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# browser = webdriver.Chrome()
# browser.get(URL)
# sleep(5)
#
# x = browser.find_element(By.ID, "input_value").text
# calculation = calc(x)
#
# result_field = browser.find_element(By.ID, "answer")
# result_field.send_keys(calculation)
#
# checkbox = browser.find_element(By.ID, "robotCheckbox")
# checkbox.click()
#
# radio_button = browser.find_element(By.ID, "robotsRule")
# radio_button.click()
#
# submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
# submit_button.click()
#
# sleep(5)


#task 4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

URL = "https://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(URL)
sleep(3)

chest = browser.find_element(By.ID, "treasure")
attribute_value = chest.get_attribute("valuex")
calculation = calc(attribute_value)

result_field = browser.find_element(By.ID, "answer")
result_field.send_keys(calculation)

checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()

radio_button = browser.find_element(By.ID, "robotsRule")
radio_button.click()

submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_button.click()

sleep(5)
