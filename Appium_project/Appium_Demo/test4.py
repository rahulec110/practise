import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_caps)
wait = WebDriverWait(driver,timeout=25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

'''Option:5th'''
driver.find_element_by_id('com.skill2lead.appiumdemo:id/Login').click()
wait.until(lambda x:x.find_element_by_android_uiautomator('text("Enter Email")')).send_keys('admin@gmail.com')
wait.until(lambda x:x.find_element_by_android_uiautomator('text("Enter Password")')).send_keys('admin123')
wait.until(lambda x:x.find_element_by_id('com.skill2lead.appiumdemo:id/Btn3')).click()
time.sleep(3)
wait.until(lambda x:x.find_element_by_class_name('android.widget.EditText')).send_keys('Rahul is using this application')
wait.until(lambda x:x.find_element_by_class_name('android.widget.Button')).click()

driver.back()
time.sleep(3)
driver.back()
time.sleep(3)

#'''Option: 6th'''
long_click_ele = wait.until(lambda x:x.find_element_by_android_uiautomator('text("LONG CLICK")'))
action = TouchAction(driver)
action.long_press(long_click_ele,5).perform()
wait.until(lambda x:x.find_element_by_class_name('android.widget.EditText')).send_keys('rahulinos98@gmail.com')
wait.until(lambda x:x.find_element_by_android_uiautomator('text("CANCEL")')).click()

time.sleep(2)
#'''Option 7'''
wait.until(lambda x:x.find_element_by_android_uiautomator('UiSelector().description("Btn8")')).click()
wait.until(lambda x:x.find_element_by_id('android:id/minutes')).click()
wait.until(lambda x:x.find_element_by_android_uiautomator('UiSelector().description("30")')).click()
driver.back()

'''Option 9'''
wait.until(lambda x:x.find_element_by_android_uiautomator('text("HYBRID")')).click()
wait.until(lambda x:x.find_element_by_id('com.skill2lead.appiumdemo:id/hEt1')).send_keys('webpage is not available')
wait.until(lambda x:x.find_element_by_android_uiautomator('text("SUBMIT")')).click()
driver.back()

'''Option 10'''
wait.until(lambda x: x.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(text("PINCH IN OUT"))')).click()
driver.back()

'''Option last'''
wait.until(lambda x:x.find_element_by_id('com.skill2lead.appiumdemo:id/autocomlete')).click()
wait.until(lambda x:x.find_element_by_android_uiautomator('text("Enter here")')).send_keys('Automation is completed on this app')
wait.until(lambda x:x.find_element_by_android_uiautomator('text("SUBMIT")')).click()

time.sleep(3)
driver.start_activity('com.google.android.youtube','com.google.android.apps.youtube.app.WatchWhileActivity')
driver.quit()