from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    input1 = browser.find_element(By.ID, "input_value")
    x = input1.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    time.sleep(2)
    driver.quit()


    # ищем элемент с текстом "Python"
# не забываем оставить пустую строку в конце файла