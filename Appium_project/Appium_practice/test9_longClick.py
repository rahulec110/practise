import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
ele = wait.until(lambda x : x.find_element_by_android_uiautomator('text("LONG CLICK")'))

action = TouchAction(driver).long_press(ele,5).perform()

wait.until(lambda x: x.find_element_by_id('com.skill2lead.appiumdemo:id/et_email').send_keys('sonimtest203@gmail.com'))
time.sleep(2)
wait.until(lambda x : x.find_element_by_android_uiautomator('text("SUBMIT")')).click()

time.sleep(3)
driver.quit()


