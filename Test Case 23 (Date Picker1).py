import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)

#apporach 1
# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("09/11/2000")
time.sleep(2)

#approach 2
year="2023"
month="April"
date="22"
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
while True:
    a=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    b=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if a==month and b==year:
        break
    else:
        driver.find_element(By.XPATH,"//a[@title='Prev']").click()

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for ele in dates:
    if ele.text==date:
        ele.click()
        break

time.sleep(2)