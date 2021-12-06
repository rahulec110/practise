from appium import webdriver


class Driver:

    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '11'
        desired_caps['deviceName'] = 'Pixel'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
        desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

        return driver
