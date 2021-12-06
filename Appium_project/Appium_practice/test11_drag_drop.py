import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['app'] = '/home/rahul/Documents/android-studio-ide-202.7351085-linux/Android_Appium_Demo.apk'
desired_caps['deviceName'] = 'SS0801'
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(text("DRAGANDDROP"))').click()

source_ele = wait.until(lambda x : x.find_element_by_id('com.skill2lead.appiumdemo:id/ingvw'))
dest_ele = wait.until(lambda x : x.find_element_by_id('com.skill2lead.appiumdemo:id/layout2'))

action = TouchAction(driver)
action.long_press(source_ele).move_to(dest_ele).release().perform()

driver.press_keycode(187)
action.tap(None,569,2176,1).perform()

time.sleep(2)
driver.quit()