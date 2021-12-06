from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

'''options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)'''

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()
driver.implicitly_wait(4)

#Case 1
click_for_js_alert = driver.find_element(By.XPATH, '(//button)[1]').click()
alert = driver.switch_to.alert
print(alert.text)
time.sleep(2)
alert.accept()
time.sleep(2)
driver.switch_to.default_content()
result = driver.find_element(By.ID, 'result')
print(result.text)

#Case 2
click_for_js_confirm = driver.find_element(By.XPATH, '(//button)[2]').click()
alert = driver.switch_to.alert
print(alert.text)
time.sleep(3)
alert.dismiss()
time.sleep(2)
driver.switch_to.default_content()
result = driver.find_element(By.ID, 'result')
print(result.text)

#Case 3
click_for_js_Prompt = driver.find_element(By.XPATH, '(//button)[3]').click()
alert = driver.switch_to.alert
print(alert.text)
time.sleep(2)
alert.send_keys('Thank you for confirmation')
alert.accept()
time.sleep(2)
driver.switch_to.default_content()
result = driver.find_element(By.ID, 'result')
print(result.text)

time.sleep(3)
driver.close()