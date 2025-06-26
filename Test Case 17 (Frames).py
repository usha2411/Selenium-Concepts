import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
driver.maximize_window()
time.sleep(5)
driver.switch_to.frame("all-packages-table")
driver.find_element(By.XPATH,"//a[normalize-space()='org.openqa.selenium']").click()
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")
driver.find_element(By.XPATH,"//a[normalize-space()='WebDriver']").click()
driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"//a[normalize-space()='Help']").click()
time.sleep(2)