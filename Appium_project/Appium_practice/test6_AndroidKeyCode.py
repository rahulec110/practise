import time
from appium import webdriver

#https://stackoverflow.com/questions/7789826/adb-shell-input-events
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'SS0801'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['apps'] = '/home/rahul/Documents/android-studio-ide-202.7351085-linux/Android_Appium_Demo.apk'
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

driver.find_element_by_id('com.skill2lead.appiumdemo:id/EnterValue').click()
time.sleep(2)
ele = driver.find_element_by_class_name('android.widget.EditText')
ele.send_keys('Rahul Sharma')
ele.click()
time.sleep(1)
'''clear character'''
driver.press_keycode(67)
driver.press_keycode(67)
time.sleep(2)

'''Home screen'''
driver.press_keycode(3)
time.sleep(3)
'''launch Recents app'''
driver.press_keycode(187)
time.sleep(2)
TouchAction(driver).tap(None,569,2176,1).perform()

'''Home screen'''
driver.press_keycode(3)
