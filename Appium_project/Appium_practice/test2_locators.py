import time

from  appium import webdriver

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'SS0801'
desired_caps['apps'] = '/home/rahul/Documents/android-studio-ide-202.7351085-linux/Android_Appium_Demo.apk'
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

'''By using ID'''
driver.find_element_by_id('com.skill2lead.appiumdemo:id/EnterValue').click()
time.sleep(2)
driver.back()
time.sleep(1)
'''By using android uiautomator'''
driver.find_element_by_android_uiautomator('UiSelector().index(4)').click()
'''By using class name'''
driver.find_element_by_class_name('android.widget.EditText').send_keys('Rahul')
'''By using text'''
#driver.find_element_by_android_uiautomator('new UiSelector().text("Enter Email")').send_keys('sonimtest203@gmail.com')
driver.find_element_by_android_uiautomator('text("Enter Email")').send_keys('sonimtest203@gmail.com')
driver.find_element_by_id('com.skill2lead.appiumdemo:id/Et6').send_keys('Ara')
driver.find_element_by_xpath('//android.widget.EditText[4]').send_keys('7725818194')
time.sleep(2)
driver.back()
'''By using content-des'''
driver.find_element_by_android_uiautomator('UiSelector().description("Btn3")').click()
time.sleep(1)
driver.back()

'''By using Xpath'''
#driver.find_element_by_xpath('//android.widget.Button[@content-desc="Btn4"]').click()


driver.find_element_by_xpath('//android.widget.Button[@index="6"]').click()
time.sleep(4)
driver.quit()
