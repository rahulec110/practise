from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

import time

def select_values(optionList, value):
    if not value[0] == 'all':
        for ele in optionList:
            print(ele.text)
            for k in range(len(value)):
                if ele.text == value[k]:
                    ele.click()
                    break
    else:
        try:
            for ele in optionList:
                ele.click()
        except Exception as e:
            print(e)
'''We are interacting 16 element out of 45 hence to handle that exception using try catch block.'''

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')
time.sleep(2)

driver.find_element(By.ID, 'justAnInputBox').click()
drop_list1 = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
value_list1 = ['all']
select_values(drop_list1, value_list1)

driver.find_element(By.CLASS_NAME, 'comboTreeArrowBtnImg').click()
time.sleep(3)

driver.find_element(By.ID, 'justAnInputBox1').click()
time.sleep(2)
drop_list2 = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
value_list2 = ['choice 2', 'choice 3', 'choice 6 2 1', 'choice 6 2 2']
select_values(drop_list2, value_list2)

time.sleep(3)
driver.find_element(By.XPATH,"(//button[@class='comboTreeArrowBtn'])[2]").click()

'''Single Selection'''
driver.find_element(By.ID,'justAnotherInputBox').click()
time.sleep(1)
drop_list3 = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
value_list3 = ['choice 6 2 2']
select_values(drop_list3, value_list3)

time.sleep(5)
driver.quit()