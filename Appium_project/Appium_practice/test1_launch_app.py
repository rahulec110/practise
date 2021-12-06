from appium import webdriver

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'SS0801'
desired_caps['app'] = '/home/rahul/Documents/android-studio-ide-202.7351085-linux/Android_Appium_Demo.apk'
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


Enter_some_value = driver.find_element_by_id('com.skill2lead.appiumdemo:id/EnterValue')
Enter_some_value.click()