import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to

driver=webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
driver.maximize_window()
driver.switch_to.frame("myFrame2")
frame1=driver.find_element(By.XPATH,"/html/body/h4").text
print(frame1)
driver.switch_to.default_content()
driver.switch_to.frame("myFrame3")
driver.find_element(By.ID,"checkBox6").click()
driver.switch_to.default_content()
driver.find_element(By.ID,"myTextInput").send_keys("Usha")
time.sleep(2)