import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def mat(x):
    return str(math.log(abs(12*math.sin(x))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
try:
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    text = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    browser.find_element(By.ID, "book").click()
    x = browser.find_element(By.ID, "input_value")
    y = mat(int(x.text))
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "#solve").click()
finally:
    time.sleep(50)
    browser.quit()

#ln(abs(12*sin(x))), where x = 95? input_value - чему равен х answer - поле для заполнения solve - кнопка
