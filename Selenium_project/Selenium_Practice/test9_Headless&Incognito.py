from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time

option = webdriver.ChromeOptions()
'''For incognito mode'''
option.add_argument('--incognito')

'''for headless browser'''
option.add_argument('--headless')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
driver.get('https://jqueryui.com/resources/demos/droppable/default.html')
print('Title of the page: ',driver.title)

time.sleep(3)
driver.close()