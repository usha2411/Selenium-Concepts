import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#accept and cancel condition
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#open alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
a= driver.switch_to.alert
print(a.text)

#accept the alert
# a.send_keys("welcome")
# a.accept()
# time.sleep(1)

#cancel the alert
a.dismiss()
time.sleep(2)

#only one ok condition
driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()

a=driver.switch_to.alert
a.accept()
time.sleep(2)