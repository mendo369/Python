from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("https://www.cursosdev.com/coupons/Spanish")

container = driver.find_element(By.CLASS_NAME, "w-screen")

cursos = container.find_elements(By.TAG_NAME, "div")

# for curso in cursos:
#     print(curso.text)

curso1 = cursos[0].find_element(By.TAG_NAME, "a")
curso1.click()

print(cursos)
# cursos[0].click()
