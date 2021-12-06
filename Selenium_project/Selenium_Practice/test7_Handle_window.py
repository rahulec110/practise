'''
1. current_window_handle() :  Returns the handle of the current window
2. window_handles()   : Returns the handles of all windows within the current session'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://opensource-demo.orangehrmlive.com/')
parent_window = driver.current_window_handle
print('Parent window name is: ', parent_window)
linkdin_link = driver.find_element(By.XPATH, '(//img[@alt])[1]')
linkdin_link.click()

child_window = driver.window_handles
print("Type of all windows: ", type(child_window))

for child in child_window:
    print(child)

    if parent_window != child:
        print('Switching to new window/tab')
        driver.switch_to.window(child)
        print('Title is: ', driver.title)
        driver.find_element(By.ID, 'email-or-phone').send_keys('rahulec110@gmail.com')
        time.sleep(3)
        #driver.close()

driver.switch_to.window(parent_window)
time.sleep(3)
print('Parent window title is : ', driver.title)
driver.find_element(By.ID, 'txtUsername').send_keys('rahuls')
time.sleep(3)
driver.quit()