from appium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_caps)
wait = WebDriverWait(driver,timeout=25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

wait.until(lambda x:x.find_element_by_id('com.skill2lead.appiumdemo:id/ScrollView')).click()

deviceSize = driver.get_window_size()
print("Device height and width size is: ",deviceSize)
screenHeight = deviceSize['height']
screenWidth = deviceSize['width']

startx1 = screenWidth/2
starty1 = screenHeight*8/9
endx1 =  screenWidth/2
endy1 = screenHeight/9

startx2 = screenWidth/2
endx2 = screenWidth/2
starty2 = screenHeight*2/9
endy2 = screenHeight*8/9

action = TouchAction(driver)
action.long_press(None,startx1,starty1).move_to(None,endx1,endy1).release().perform()
time.sleep(3)

action.long_press(None,startx2,starty2).move_to(None,endx2,endy2).release().perform()
time.sleep(3)

driver.quit()