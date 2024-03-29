from selenium import webdriver
import time
from math import sin, log               # Необходим, тк в процессе вырезаем функции с сайта

driver = webdriver.Chrome()
driver.get('https://suninjuly.github.io/redirect_accept.html')

# Locators
BUTTON_TROLLFACE_LOCATOR = ('class name', 'trollface')
EXPRESSION_FIELD_LOCATOR = ('id', 'answer')
EXPRESSION_LOCATORS = ('css selector', 'nowrap')
X_EXPRESSION_LOCATOR = ('id', 'input_value')
BUTTON_SUBMIT = ('css selector', 'button.btn-primary')

# 1st step page
driver.find_element(*BUTTON_TROLLFACE_LOCATOR).click()

tabs = driver.window_handles
driver.switch_to.window(tabs[1])
# Ваш код, который заполняет обязательные поля
x_to_replace = int(driver.find_element(*X_EXPRESSION_LOCATOR).text)
expression = log(abs(12*sin(x_to_replace)))
driver.find_element(*EXPRESSION_FIELD_LOCATOR).send_keys(expression)

# Отправляем заполненную форму
driver.find_element(*BUTTON_SUBMIT).click()
time.sleep(3)