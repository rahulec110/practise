import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'SS0801'
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
wait = WebDriverWait(driver,timeout=25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

print('Device width and Hieight : ',driver.get_window_size())
deviceSize = driver.get_window_size()
screenHeight = deviceSize['height']
screenWidth =  deviceSize['width']

'''Scroll Up to down'''
startx1= screenWidth/2
endx1 = screenWidth/2
starty1 = screenHeight*8/9
endy1= screenHeight/9

'''scrolling  down to Up'''
startx2= screenWidth/2
endx2 = screenWidth/2
starty2= screenHeight*2/9
endy2 = screenHeight*8/9

action = TouchAction(driver)
action.long_press(None,startx1, starty1).move_to(None,endx1,endy1).release().perform()
time.sleep(3)

action.long_press(None,startx2,starty2).move_to(None,endx2,endy2).release().perform()
time.sleep(2)

'''Home screen'''
driver.press_keycode(3)
time.sleep(1)