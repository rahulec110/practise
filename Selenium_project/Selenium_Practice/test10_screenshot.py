from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

option = webdriver.ChromeOptions()
#option.add_argument('--incognito')
option.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.youtube.com/')

driver.get_screenshot_as_file('test.png')

'''screenshot for full page need to run in headless mode'''
s= lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(s('Width'),s('Height'))
driver.find_element(By.ID, 'content').screenshot('youtube.png')

time.sleep(2)
driver.close()