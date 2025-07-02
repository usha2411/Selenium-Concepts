#after open focus should shift in new window
import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window()
driver.get("https://www.facebook.com/")

time.sleep(5)
