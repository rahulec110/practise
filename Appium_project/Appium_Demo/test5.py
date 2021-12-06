import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['deviceName'] = 'Pixel'
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
wait = WebDriverWait(driver,timeout=25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

wait.until(lambda x:x.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(text("AUTO SUGGESTION"))'))

ele = driver.find_elements_by_class_name('android.widget.Button')
print('No of element: ', len(ele))
for x in ele:
    button = x.text
    print(button)
    if button == 'DRAGANDDROP':
        x.click()
        break

sorce_ele = wait.until(lambda x:x.find_element_by_id("com.skill2lead.appiumdemo:id/ingvw"))
des_ele = wait.until(lambda x:x.find_element_by_id('com.skill2lead.appiumdemo:id/layout3'))

action = TouchAction(driver)
action.long_press(sorce_ele).move_to(des_ele).release().perform()
'''
print('Is device is locked: ',driver.is_locked())
print('Current package name',driver.current_package)
print('Current package activity name:', driver.current_activity)

print('Current device orientation: ', driver.orientation)'''
time.sleep(2)
