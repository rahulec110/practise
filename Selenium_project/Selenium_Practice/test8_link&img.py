from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.makemytrip.com/')

link = driver.find_elements(By.TAG_NAME, 'a')
print('No of links: ',len(link))
for ele in link:
    print(ele.text)
    print(ele.get_attribute('href'))

img = driver.find_elements(By.TAG_NAME, 'img')
print('No of image: ',len(img))
for ele in img:
    print(ele.get_attribute('src'))

time.sleep(1)
driver.quit()