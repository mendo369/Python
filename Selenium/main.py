from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("https://orbitia.app/")

search = driver.find_element(By.CSS_SELECTOR, '[class="form-search"]')
search.click()

send = driver.find_element(By.CSS_SELECTOR, '[class="fa fa-search"]')

input = driver.find_element(By.CSS_SELECTOR, '[id="wabaNumber"]')
input.send_keys("3176021791")

send.click()

