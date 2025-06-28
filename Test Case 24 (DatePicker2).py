import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='dob']").click()

a=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
a.select_by_visible_text("Nov")

b=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
b.select_by_visible_text("2006")

dates=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")
for ele in dates:
    if ele.text=="25":
        ele.click()
        break

time.sleep(2)