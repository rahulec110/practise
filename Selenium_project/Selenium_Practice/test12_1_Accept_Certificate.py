from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import time
'''Option: 1'''
#options = Options()
#options.add_argument('--allow-running-insecure-content')
#options.add_argument('--ignore-certificate-errors')
#driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)

'''Option : 2'''
#desired_capabilities = DesiredCapabilities().CHROME.copy()
#desired_capabilities['acceptInsecureCerts'] = True
#driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities = desired_capabilities)

'''Option: 3'''
options = Options()
options.set_capability('acceptInsecureCerts', True)
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = options)
driver.implicitly_wait(5)

driver.get('https://pjira.oneplus.cn/jira/secure/Dashboard.jspa')
driver.find_element(By.NAME, 'os_username').send_keys('v-rahul.s')
time.sleep(3)
driver.back()
alert = driver.switch_to.alert
alert.accept()
time.sleep(3)
driver.get('https://pcf.oneplus.cn/')


time.sleep(3)
driver.close()
