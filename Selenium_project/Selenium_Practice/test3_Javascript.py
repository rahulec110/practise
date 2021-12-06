from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

option = webdriver.ChromeOptions()
option.add_argument('--incognito')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=option )
driver.implicitly_wait(10)
driver.maximize_window()
driver.delete_all_cookies()

driver.get('https://www.amazon.in/')
'''we can use for click operation: "arguments[0].click();"    '''
best_sellers = driver.find_element(By.XPATH, "(//a[text()='Best Sellers'])[1]")
driver.execute_script("arguments[0].click();", best_sellers)
time.sleep(3)

driver.back()

'''Refreash the page by using javasript : history.go(0);'''
driver.execute_script("history.go(0);")
time.sleep(2)

'''Get the title page: return document.title; '''
title = driver.execute_script("return document.title;")
print('Title of the page: ', title)

'''Print all text of current page '''
all_text = driver.execute_script("return document.documentElement.innerText;")
print(len(all_text))
print(all_text)

'''To create a border around the element'''
fashion_ele = driver.find_element(By.LINK_TEXT, 'Fashion')
driver.execute_script("arguments[0].style.border = '3px solid red'",fashion_ele)
time.sleep(2)

'''To scroll down buttom of the page'''
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(3)
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
time.sleep(5)

'''To take a screenshot'''
driver.get_screenshot_as_file('test.png')
time.sleep(1)

'''To scroll till mentioned element'''
ele = driver.find_element(By.XPATH, "(//h2[@class='as-title-block-left'])[3]")
driver.execute_script("arguments[0].scrollIntoView(true);", ele)

'''Note: we can also perform sendkey operation by using javascriptexecuter'''

'''To take full page screenshot'''
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot('amazon.png')

time.sleep(3)
driver.close()