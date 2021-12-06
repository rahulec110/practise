import time

from appium import webdriver

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'SS0801'
desired_caps['apps'] = '/home/rahul/Documents/android-studio-ide-202.7351085-linux/Android_Appium_Demo.apk'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
element = driver.find_elements_by_class_name('android.widget.Button')
print('Length of buttons: ',len(element))
for x in element:
    button = x.text
    print(button)
    if button == 'LOGIN':
        x.click()
        break
time.sleep(8)
driver.quit()