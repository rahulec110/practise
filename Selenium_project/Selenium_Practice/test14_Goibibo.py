from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.goibibo.com/')
print('Title of the page: ', driver.title)

'''Identifying and click on from segment'''
print('----------------Identifying and click on from segment------------------')
driver.find_element(By.ID,'gosuggest_inputSrc').send_keys('Patna')
list_elements_From = driver.find_elements(By.XPATH,"//li[contains(@id,'react-autosuggest-1-suggestion')]//div[@class='mainTxt clearfix']/span")
print(len(list_elements_From))
for ele in list_elements_From:
    print(ele.text)
    if ele.text == 'Gaya, India':
        print('-------------------------Matched found------------------------\n')
        ele.click()
        break

time.sleep(1)

'''Identifying and click on To segment'''
print('Identifying and click on To segment')
driver.find_element(By.XPATH, "//input[@placeholder='Destination']").send_keys('banga')
list_elements_To = driver.find_elements(By.XPATH, "//li[contains(@id,'react-autosuggest-1-suggestion')]//div[@class='mainTxt clearfix']/span")
print(len(list_elements_To))
for ele in list_elements_To:
    print(ele.text)
    if ele.text == 'Delhi, India':
        ele.click()
        break

'''Day-Picker'''
driver.find_element(By.XPATH, "//span[@aria-label='Next Month']").click()
date = driver.find_element(By.XPATH,"//div[@aria-label='Mon Jul 05 2021']")
date.click()

driver.find_element(By.ID, 'returnCalendar').click()
list_date_elements = driver.find_elements(By.XPATH, "//div[@class='calDate']")
print("Length= ",len(list_date_elements))
for dateelement in list_date_elements:
    date = dateelement.text
    print(date)
    if date == '''10
4485''':
        dateelement.click()
        break

time.sleep(2)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(3)
driver.close()