import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com/')

wait = WebDriverWait(driver,timeout=20,poll_frequency=1,ignored_exceptions=(NoSuchElementException,))
title_status = wait.until(ec.title_is('Google'))
print('Title is matched: ',title_status)
wait.until(lambda x:x.find_element(By.CSS_SELECTOR,"input[class='gLFyf gsfi']")).send_keys('python')

option_list = wait.until(lambda x:x.find_elements_by_css_selector('ul.erkvQe li span'))
print(len(option_list))
for ele in option_list:
    print(ele.text)
    if ele.text == 'python install':
        ele.click()
        break

time.sleep(3)
wait.until(lambda x:x.find_element_by_partial_link_text(' › downloads')).click()

about_ele = wait.until(lambda x:x.find_element(By.ID,'about'))
action = ActionChains(driver)
action.move_to_element(about_ele).perform()
wait.until(lambda x:x.find_element(By.LINK_TEXT, "Applications")).click()
time.sleep(3)
driver.quit()