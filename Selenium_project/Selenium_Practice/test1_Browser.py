from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time

'''time out = 10
dynamic wait 
imp wait will be applied for all the web elements
global wait
find element
find elements
only for web elements
not for non web elements : title, url, alerts'''

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.google.com')
print("Title of the page: ", driver.title )

driver.find_element(By.NAME, 'q').send_keys('python')
time.sleep(2)
option_list = driver.find_elements(By.CSS_SELECTOR, "ul.erkvQe li span")
print(len(option_list))

for ele in option_list:
    print(ele.text)
    if ele.text == 'python install':
        ele.click()
        break

driver.find_element(By.PARTIAL_LINK_TEXT, 'Download Python | Python.org').click()
time.sleep(2)

about_ele = driver.find_element(By.XPATH, "(//a[text()='About'])[1]")
act_chains = ActionChains(driver)
act_chains.move_to_element(about_ele).perform()
driver.find_element(By.LINK_TEXT, 'Getting Started').click()
time.sleep(3)
'''
driver.back()

time.sleep(3)
about_ele = driver.find_element(By.XPATH, "(//a[text()='About'])[1]")
act_chains = ActionChains(driver)
act_chains.move_to_element(about_ele).perform()
driver.find_element(By.LINK_TEXT, 'Quotes').click()


time.sleep(5)
driver.close()'''