import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_cap= {}

desired_cap['platformName'] = 'Android'
desired_cap['platformVersion'] = '11'
desired_cap['deviceName'] = 'SS0801'
desired_cap['appPackage'] = 'com.skill2lead.appiumdemo'
desired_cap['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)

wait = WebDriverWait(driver,timeout=25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
ele = wait.until(lambda x : x.find_element_by_id('com.skill2lead.appiumdemo:id/TabView'))
ele.click()

print('Device width and Height: ',driver.get_window_size())
deviceSize = driver.get_window_size()
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']

'''Right to left'''
startx1 = screenWidth*8/9
endx1 = screenWidth/9
starty1 = screenHeight/2
endy1 = screenHeight/2

'''Left to right'''
startx2 = screenWidth/9
endx2 = screenWidth*8/9
starty2 = screenHeight/2
endy2 = screenHeight/2

action = TouchAction(driver)
action.long_press(None,startx1,starty1).move_to(None,endx1,endy1).release().perform()

time.sleep(3)
action.long_press(None,startx2,starty2).move_to(None,endx2,endy2).release().perform()
time.sleep(1)

'''Home screen'''
driver.press_keycode(3)
time.sleep(1)
