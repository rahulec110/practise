import time
from selenium import webdriver

'''
1. Install the pytest-xdist(pip install pytest-xdist)
2. Add udid and systemPort in desired capabilities
3. Run the file using command as: pytest -n <numprocess>
>> Port should be 8200-8299
'''

#Step 1: Create Desired capabilities
def deviceDriver(deviceId, sysPort):
    desired_caps = {}

    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['platformVersion'] = '11'
    desired_caps['systemPort'] = sysPort
    desired_caps['udId'] = deviceId
    desired_caps['apps'] = '/home/rahul/Documents/android-studio-ide-202.7351085-linux/Android_Appium_Demo.apk'
    desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
    desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'


    #Step 2: Create driver object
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver

def enterText(driver):
    #Step 3: Click on the button by using ID locator
    driver.find_element_by_id('com.skill2lead.appiumdemo:id/EnterValue').click()
    time.sleep(3)

    '''By using class name'''
    ele_className = driver.find_element_by_id('com.skill2lead.appiumdemo:id/Et1')
    ele_className.click()
    ele_className.send_keys('Rahul')
    time.sleep(4)

    driver.quit()

def test_DeviceTest():
    d1 = deviceDriver('emulator-5556', 8200)
    d2 = deviceDriver('emulator-5554', 8201)

    enterText(d1)
    enterText(d2)
