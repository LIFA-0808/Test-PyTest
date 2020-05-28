from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time
import math


def calc(num):
    return str(math.log(abs(12*math.sin(int(num)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока цена не станет 100$
    button = browser.find_element_by_id('book')
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button.click()

    # находим элемент и делаем расчёт
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # вводим ответ
    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)

    button = browser.find_element_by_css_selector("button[type=submit]")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
