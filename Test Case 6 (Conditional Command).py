#is_displayed()
#is_enabled()
#is_selected()
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

#is-displayed
a=driver.find_element(By.XPATH,"//input[@id='small-searchterms']").is_displayed()
print("Displayed:",a)

#is-enabled
b=driver.find_element(By.XPATH,"//input[@id='small-searchterms']").is_enabled()
print("Enabled:",b)

#is_selected
c=driver.find_element(By.XPATH,"//input[@id='gender-male']").is_selected()
print("Male is selected:",c)
driver.find_element(By.XPATH,"//input[@id='gender-male']").click()
time.sleep(2)

d=driver.find_element(By.XPATH,"//label[normalize-space()='Female']").is_selected()
print("Female is selected:",d)
driver.find_element(By.XPATH,"//label[normalize-space()='Female']").click()


rd=driver.find_element(By.XPATH,"//input[@id='gender-male']")
print(rd.is_selected())
rd.click()
print(rd.is_selected())