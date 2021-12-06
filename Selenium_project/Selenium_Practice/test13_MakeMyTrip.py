from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.makemytrip.com/flights/')
time.sleep(1)
print(driver.title)
'''Identifying From element'''
driver.find_element(By.ID, 'fromCity').click()
driver.find_element(By.XPATH, "//input[@placeholder='From']").send_keys('Banga')
time.sleep(2)
option_list1 = driver.find_elements(By.XPATH,"//p[@class='font14 appendBottom5 blackText']")
for ele in option_list1:
    print(ele.text)
option_list = driver.find_elements(By.XPATH,"//p[@class='font12 greyText appendBottom3']")
print('Total suggestions are: ',len(option_list))
for ele in option_list:
    print(ele.text)
    if ele.text == 'Kempegowda International Airport':
        ele.click()
        break
time.sleep(2)

'''Identifying To element'''
driver.find_element(By.ID, 'toCity').click()
driver.find_element(By.XPATH, "//input[@placeholder='To']").send_keys('Patna')
time.sleep(1)
option_lst1 = driver.find_elements(By.XPATH,"//p[@class='font14 appendBottom5 blackText']")
for ele in option_lst1:
    print(ele.text)

option_lst = driver.find_elements(By.XPATH, "//p[@class='font12 greyText appendBottom3']")
for ele in option_lst:
    print(ele.text)
    if ele.text == 'Lok Nayak Jayaprakash Airport':
        ele.click()
        break
'''Selecting date'''
next_month = driver.find_element(By.XPATH,"//span[@aria-label='Next Month']")
next_month.click()
driver.find_element(By.XPATH,"//div[@aria-label='Fri Jul 02 2021']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//p[@data-cy='submit']").click()

time.sleep(3)
driver.close()