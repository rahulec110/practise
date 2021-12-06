from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

option = webdriver.ChromeOptions()
option.add_argument('--incognito')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
driver.maximize_window()
driver.implicitly_wait(10)

def select_option(option_list, values):
    for ele in option_list:
        print(ele.text)
        for k in range(len(values)):
            if ele.text == values[k]:
                ele.click()
                break


driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')

driver.find_element(By.ID, 'justAnInputBox').click()
drop_list1 = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
value_list1 = ['choice 2', 'choice 3', 'choice 6 2 1', 'choice 6 2 2']
select_option(drop_list1, value_list1)
time.sleep(2)

driver.find_element(By.CLASS_NAME, 'comboTreeArrowBtnImg').click()
time.sleep(3)

'''Multi Selection With Cascade Option Select'''
driver.find_element(By.ID, 'justAnInputBox1').click()
drop_list2 = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
value_list2 = ['choice 2 1', 'choice 2 2', 'choice 6 2 1', 'choice 6 2 2']
select_option(drop_list2, value_list2)
time.sleep(2)
driver.find_element(By.XPATH,"(//button[@class='comboTreeArrowBtn'])[2]").click()
time.sleep(3)

'''Single Selection'''
driver.find_element(By.ID,'justAnotherInputBox').click()
time.sleep(1)
drop_list3 = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
value_list3 = ['choice 6 2 2']
select_option(drop_list3, value_list3)

time.sleep(3)
driver.close()