#task 1
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# URL = "http://suninjuly.github.io/cats.html"
#
# try:
#     driver = webdriver.Chrome()
#     driver.get(URL)
#     driver.find_element(By.ID, "button")
# finally:
#     driver.quit()


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#task 2
URL = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(URL)
    button = WebDriverWait(driver, 12).until(
     EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    book_button = driver.find_element(By.ID, "book")
    book_button.click()

    x = driver.find_element(By.ID, "input_value").text
    calculation = calc(x)
    answer_field = driver.find_element(By.ID, "answer")
    driver.execute_script("return arguments[0].scrollIntoView(true);", answer_field)
    answer_field.send_keys(calculation)
    solve_button = driver.find_element(By.ID, "solve")
    solve_button.click()
    sleep(4)

finally:
    driver.quit()