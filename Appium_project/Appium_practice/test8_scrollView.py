import time

from appium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps= {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'SS0801'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
ele1 = wait.until(lambda x : x.find_element_by_android_uiautomator('text("ScrollView")'))
ele1.click()
wait.until(lambda x : x.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON13"))')).click()
wait.until(lambda y : y.find_element_by_android_uiautomator('text("YES")')).click()
driver.quit()


