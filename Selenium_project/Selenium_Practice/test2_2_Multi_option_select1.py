from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

option = webdriver.ChromeOptions()
option.add_argument('--incognito')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
driver.maximize_window()
driver.implicitly_wait(10)
driver.delete_all_cookies()

driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')
time.sleep(3)
driver.find_element(By.ID,'justAnInputBox').click()
time.sleep(2)

drop_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')

for ele in drop_list:
    print(ele.text)
    if ele.text == 'choice 3':
        ele.click()
        break

time.sleep(3)
driver.close()
