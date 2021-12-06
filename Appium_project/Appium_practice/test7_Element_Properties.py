import time

from appium import webdriver

desired_caps= {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'SS0801'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['apps'] = '/home/rahul/Documents/android-studio-ide-202.7351085-linux/Android_Appium_Demo.apk'
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

button = driver.find_element_by_xpath('//android.widget.Button[@content-desc="Btn1"]')
print('Is displayed : ', button.is_displayed())
print('Is enable : ', button.is_enabled())
print('Is Selected: ',button.is_selected())
print('Size is : ',button.size)
print('location is : ', button.location)
print('Text of the button is: ',button.text)
print('Text of the button is: ',button.get_attribute('text'))
print('Content description: ',button.get_attribute('content-desc'))
time.sleep(5)

button.click()
time.sleep(4)
ele = driver.find_element_by_id('com.skill2lead.appiumdemo:id/Et1')
ele.send_keys('Rahul Sharma')
time.sleep(2)
ele.clear()
time.sleep(2)
'''Home screen'''
driver.press_keycode(3)
