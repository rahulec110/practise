from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

import time

'''Option : 1'''
profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True

'''Option: 2'''
#desired_capabilities = DesiredCapabilities.FIREFOX.copy()
#desired_capabilities['acceptInsecureCerts'] = True
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), capabilities=desired_capabilities)

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://pjira.oneplus.cn/jira/secure/Dashboard.jspa')
driver.find_element(By.NAME, 'os_username').send_keys('v-rahul.s')

time.sleep(3)
driver.close()