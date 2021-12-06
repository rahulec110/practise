from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time
#http://allselenium.info/working-with-expected-conditions-explicit-wait-part-2/


option = webdriver.ChromeOptions()
option.add_argument('incognito')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)

driver.get('https://www.freshworks.com/')

wait = WebDriverWait(driver, 10)
'''Display all the text in footer'''
footer_links = wait.until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, 'ul.footer-nav li')))
print(len(footer_links))

for ele in footer_links:
    print(ele.text)

'''
Case 1:
driver.get('http://the-internet.herokuapp.com/javascript_alerts')
click_for_js_alert = driver.find_element(By.XPATH, '(//button)[1]').click()
wait = WebDriverWait(driver, 10)
alert = wait.until(ec.alert_is_present())
print(alert.text)
alert.accept()

Case 2:

driver.get('https://zentreeindia.tsheets.com/page/login')

wait = WebDriverWait(driver, 10)
wait.until(ec.element_to_be_clickable((By.ID, 'login_signin')))
print()

username= wait.until(ec.visibility_of_element_located((By.NAME, 'username')))
username.send_keys('rahulsharama')

#wait.until(ec.title_contains('QuickBooks Time :: login'))
#wait.until(ec.title_is('QuickBooks Time :: login'))
print(driver.title)
#Username = wait.until(ec.presence_of_element_located((By.NAME, 'username')))
#Username.send_keys('rahul')

'''


time.sleep(2)
driver.close()