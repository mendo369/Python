from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("https://es.pornhub.com/")

#search = driver.find_element(By.CSS_SELECTOR, '[id="searchInput"]')
#search.send_keys("white")
#search.send_keys(Keys.ENTER)

livePorn = driver.find_element(By.CSS_SELECTOR, '[id="menuItem3"]')
livePorn.click()

driver.implicitly_wait(10)

elements = driver.find_element(By.CSS_SELECTOR, '[class="js-mxp"]')
for elemet in elements


