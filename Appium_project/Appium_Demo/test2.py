import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['deviceName'] = 'Pixel'
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_caps)
wait = WebDriverWait(driver,timeout=25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

wait.until(lambda x:x.find_element_by_id('com.skill2lead.appiumdemo:id/TabView')).click()

print('Device width and height :',driver.get_window_size())
deviceSize = driver.get_window_size()
screenWidth= deviceSize['width']
screenHeight= deviceSize['height']

'''Right to left'''
startx1 = screenWidth*8/9
endx1 = screenWidth/9
starty1 = screenHeight/2
endy1 = screenHeight/2

'''Left to Right'''
startx2 = screenWidth/9
endx2 = screenWidth*8/9
starty2 = screenHeight/2
endy2 = screenHeight/2


'''swiping Right to left'''
action = TouchAction(driver)
action.long_press(None,startx1,starty1).move_to(None,endx1,endy1).release().perform()
time.sleep(2)
action.long_press(None,startx1,starty1).move_to(None,endx1,endy1).release().perform()
time.sleep(2)

'''Swiping left to Right'''
action.long_press(None,startx2,starty2).move_to(None,endx2,endy2).release().perform()
time.sleep(2)
action.long_press(None,startx2,starty2).move_to(None,endx2,endy2).release().perform()
time.sleep(2)

driver.quit()
