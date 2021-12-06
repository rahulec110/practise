from appium import webdriver

class Driver:

    def getDriverMethod(self):
        desired_caps= {}

        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '11'
        desired_caps['deviceName'] = 'OnePlus Nord'
        desired_caps['automationName'] = 'UiAutomator2'
        #desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
        #desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

        desired_caps['appPackage'] = 'com.oneplus.camera'
        desired_caps['appActivity'] = 'com.oneplus.camera.OPCameraActivity'

        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

        return driver

    # 1. To check Driver class is working correctly or not we need to check from file under Test package
    # 2. Create Customlogger file under utilities Pacjkage and call this from file under Tests package
    # 3. Now we will create BasePage class....where will write all the method to identify and wait untill locator is displayed.
