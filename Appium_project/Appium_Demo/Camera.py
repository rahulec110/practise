import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['deviceName'] = 'OnePlus 9R'
desired_caps['appPackage'] = 'com.oneplus.camera'
desired_caps['appActivity'] = 'com.oneplus.camera.OPCameraActivity'


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities= desired_caps)
wait = WebDriverWait(driver,timeout=20,poll_frequency=2,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
wait.until(lambda x: x.find_element_by_android_uiautomator('UiSelector().index(0)')).click()

'''To Capture an image'''
wait.until(lambda x:x.find_element_by_android_uiautomator('text("PHOTO")')).click()
driver.press_keycode(27)
wait.until(lambda x:x.find_element_by_android_uiautomator('text("GOT IT")')).click()

'''To Recording video with Pause for 2 sec'''
record_video = wait.until(lambda x:x.find_element_by_android_uiautomator('text("VIDEO")'))
record_video.click()
driver.press_keycode(27)
time.sleep(10)
Pause = driver.find_element_by_xpath('(//android.widget.ImageButton[@content-desc="Snapshot"])[1]')
Cap_img = driver.find_element_by_id('com.oneplus.camera:id/secondary_button')
for x in range(2):
    Pause.click()
    time.sleep(2)
    Pause.click()
    Cap_img.click()
    time.sleep(8)
driver.press_keycode(27)

'''Slow motion video'''
slow_video = wait.until(lambda x:x.find_element_by_android_uiautomator('text("SLOW MOTION")'))
slow_video.click()
driver.press_keycode(27)
time.sleep(5)
driver.press_keycode(27)

'''Time lapse video'''
wait.until(lambda x:x.find_element_by_android_uiautomator('text("TIME-LAPSE")')).click()
driver.press_keycode(27)
time.sleep(5)
driver.press_keycode(27)

'''Navigating to Portrait & NightScape mode'''
slow_video.click()
record_video.click()
wait.until(lambda x:x.find_element_by_android_uiautomator('text("PORTRAIT")')).click()
time.sleep(3)
driver.press_keycode(27)
time.sleep(5)
wait.until(lambda x:x.find_element_by_android_uiautomator('text("NIGHTSCAPE")')).click()
time.sleep(3)
driver.press_keycode(27)


