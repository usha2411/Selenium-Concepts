from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
a=driver.find_element(By.XPATH,"//input[@id='Email']")
a.clear()
a.send_keys("usha@gmail.com")

print("Result of text:",a.text)
print("Result of grt attribute:",a.get_attribute("value"))

b=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("Result of text:",b.text)
print("Result of get attribute:",b.get_attribute("value"))
print("Result of get attribute:",b.get_attribute("type"))