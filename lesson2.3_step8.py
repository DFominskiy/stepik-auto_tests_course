import math
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    btn = browser.find_element_by_xpath('//*[@id="book"]')
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    btn.click()
    x = browser.find_element_by_xpath('//span[@id="input_value"]')
    browser.execute_script("arguments[0].scrollIntoView(true);", x)
    input_field = browser.find_element_by_xpath(('//input[@id="answer"]'))
    value = calc(x.text)
    input_field.send_keys(value)
    submit = browser.find_element_by_xpath('//button[text()="Submit"]')
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
