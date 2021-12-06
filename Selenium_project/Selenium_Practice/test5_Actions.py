''' 1. we can able to send text by using send_keys_to_element(loctors, 'text'):
act_chains.send_keys_to_element(UserName, 'rahulsharma@zentreelabs.com')
    2. Able to perform click operation by using click(locators).perform()
act_chains.click(ClickOn_SignIn).perform()
    3. Able to move the cursor from one element to another element by using move_to_element(locators).perform()
act_chains = ActionChains(driver)
act_chains.move_to_element(clickOn_TimeSheet).perform()
driver.find_element(By.LINK_TEXT, 'Time Entries').click()
    4. Able to perform Right click on particular element
act_chain = ActionChains(driver)
act_chain.context_click(right_click_ele).perform()'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

driver.get('https://jqueryui.com/resources/demos/droppable/default.html')
drag_ele = driver.find_element(By.ID,'draggable')
print(drag_ele.text)

drop_ele = driver.find_element(By.ID, 'droppable')
print(drop_ele.text)

act_chains = ActionChains(driver)
act_chains.click_and_hold(drag_ele).move_to_element(drop_ele).release().perform()

'''
# Use sen_keys by using Action class
driver.get('https://zentreeindia.tsheets.com/page/login')
UserName = driver.find_element(By.XPATH, "//input[@name='username']")
PassWord = driver.find_element(By.XPATH, "//input[@name='password']")
ClickOn_SignIn = driver.find_element(By.CSS_SELECTOR, "#login_signin")

act_chains = ActionChains(driver)
act_chains.send_keys_to_element(UserName, 'rahulsharma@zentreelabs.com')
act_chains.send_keys_to_element(PassWord, '123456')
act_chains.click(ClickOn_SignIn).perform()'''

time.sleep(2)
driver.close()