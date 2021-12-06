from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'SS0801'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

print('Is device is locked ? (Yes/No)  ',driver.is_locked())
print('Current Package name: ',driver.current_package)
print('Current Activity name: ',driver.current_activity)
print('Current context: ',driver.current_context)
print('Current orirntation is: ',driver.orientation)