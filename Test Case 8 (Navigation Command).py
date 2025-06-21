#back()
#forward()
#refresh()
import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.in/")
driver.back()
driver.forward()
driver.refresh()
time.sleep(3)
driver.quit()