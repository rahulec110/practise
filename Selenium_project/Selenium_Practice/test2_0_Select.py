from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time

browsername = 'chrome'

if browsername == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browsername == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print('Please Pass the correct browser name ', browsername)
    raise Exception('Driver is not found.......')

driver.get("https://www.facebook.com/")
driver.implicitly_wait(4)
driver.maximize_window()
time.sleep(2)
driver.find_element_by_link_text('English (UK)').click()
time.sleep(3)
driver.find_element(By.LINK_TEXT, 'Create New Account').click()
time.sleep(4)

def select_values(element, values):
    select = Select(element)
    select.select_by_visible_text(values)

driver.find_element(By.NAME, 'firstname').send_keys('Archit')
time.sleep(1)
driver.find_element(By.NAME, 'lastname').send_keys('Rai')
driver.find_element(By.NAME, 'reg_email__').send_keys('sonimtest203@gmail.com')
time.sleep(2)
driver.find_element(By.NAME,'reg_email_confirmation__').send_keys('sonimtest203@gmail.com')
driver.find_element(By.NAME, 'reg_passwd__').send_keys('sonimtest123')

date = driver.find_element(By.ID, 'day')
select_values(date,'2')
time.sleep(2)
month = driver.find_element(By.ID, 'month')
select_values(month,'Dec')
time.sleep(2)
year = driver.find_element(By.ID, 'year')
select_values(year,'1995')

time.sleep(2)
driver.find_element(By.XPATH,"//label[text()='Male']").click()

'''date = driver.find_element(By.ID, 'day')
Select(date).select_by_visible_text('2')
time.sleep(2)

month = driver.find_element(By.ID, 'month')
Select(month).select_by_visible_text('Dec')
time.sleep(2)

year = driver.find_element(By.ID, 'year')
Select(year).select_by_visible_text('1995')'''

time.sleep(3)
driver.close()