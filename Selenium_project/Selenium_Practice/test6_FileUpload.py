from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')

# Note: type = 'file'  must be present then we can use
driver.find_element(By.NAME, 'photo').send_keys('/home/rahul/Pictures/Screenshot from 2021-04-09 15-50-05.png')

'''driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')

driver.find_element(By.NAME, 'upfile').send_keys('/home/rahul/Pictures/Screenshot from 2021-04-09 15-50-05.png')
driver.find_element(By.XPATH, "//input[@type='submit']").click()'''

time.sleep(3)
driver.close()