import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.get("https://www.facebook.com/r.php/")
driver.maximize_window()

a=Select(driver.find_element(By.XPATH,"//select[@id='day']"))

#select one option
a.select_by_visible_text("1")
a.select_by_value("2")
a.select_by_index(4)

#capture all options
c=Select(driver.find_element(By.XPATH,"//select[@id='month']"))
b=c.options
print(len(b))

for i in b:
    print(i.text)

#select dropdown value without using built in fun
x=Select(driver.find_element(By.XPATH,"//select[@id='year']"))
y=x.options
for i in y:
    if i.text=="2021":
        i.click()