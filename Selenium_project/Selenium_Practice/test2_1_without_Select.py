from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com/")
driver.implicitly_wait(4)
driver.find_element(By.LINK_TEXT, 'Create New Account').click()
time.sleep(4)

'''def select_dropdown_values(list_option, values):
    print(len(list_option))
    for ele in list_option:
        print(ele.text)
        if ele.text == values:
            ele.click()
            break'''

day_ele = driver.find_elements(By.XPATH, "//select[@id='day']/option")
print(len(day_ele))
for ele in day_ele:
    print(ele.text)
    if ele.text == '25':
        ele.click()
        break

'''day_ele = driver.find_elements(By.XPATH, "//select[@id='day']/option")
select_dropdown_values(day_ele, '23')

month_ele = driver.find_elements(By.XPATH, "//select[@id='month']/option")
select_dropdown_values(month_ele, 'Dec')

year_ele = driver.find_elements(By.XPATH, "//select[@id='year']/option")
select_dropdown_values(year_ele, '2019')'''

time.sleep(3)
driver.close()