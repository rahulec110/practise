from appium import webdriver
import time

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['deviceName'] = 'Pixel'
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(5)

driver.start_activity('com.google.android.youtube', 'com.google.android.apps.youtube.app.WatchWhileActivity')
time.sleep(4)

driver.start_activity('com.android.camera2', 'com.android.camera.CameraLauncher')
time.sleep(3)

driver.start_activity('com.skill2lead.appiumdemo', 'com.skill2lead.appiumdemo.MainActivity')
time.sleep(3)

driver.quit()

