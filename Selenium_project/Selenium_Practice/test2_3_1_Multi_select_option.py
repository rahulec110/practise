from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

option = webdriver.ChromeOptions()
option.add_argument('--incognito')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
driver.implicitly_wait(10)
driver.maximize_window()

def select_values(option_list, value):
    for ele in option_list:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break

driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')
time.sleep(2)
'''Multi Selection'''
driver.find_element(By.ID, 'justAnInputBox').click()
drop_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
select_values(drop_list,'choice 2')
select_values(drop_list, 'choice 4')
time.sleep(2)

driver.find_element(By.CLASS_NAME, 'comboTreeArrowBtnImg').click()
time.sleep(3)

'''Multi Selection With Cascade Option Select'''
driver.find_element(By.ID, 'justAnInputBox1').click()
drop_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
select_values(drop_list, 'choice 3')
select_values(drop_list, 'choice 4')
select_values(drop_list, 'choice 5')
time.sleep(2)

'''driver.find_element(By.CLASS_NAME, 'comboTreeArrowBtnImg').click()
time.sleep(3)'''

'''Single Selection'''
driver.find_element(By.ID,'justAnotherInputBox').click()
time.sleep(1)
drop_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
select_values(drop_list, 'choice 6 2 1')

time.sleep(3)
driver.close()

