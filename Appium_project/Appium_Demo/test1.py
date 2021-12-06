import time
from appium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['deviceName'] = 'Pixel'
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_caps)
wait = WebDriverWait(driver,timeout=20,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

"""Option 1st"""
Enter_some_value = driver.find_element_by_id('com.skill2lead.appiumdemo:id/EnterValue')
Enter_some_value.click()
filed_text = wait.until(lambda x :x.find_element_by_id('com.skill2lead.appiumdemo:id/Et1').send_keys('rahulsharma@zentreelabs.com'))
filed_text.clear()
filed_text.send_keys('0133ec131110')
'''By using text'''
#driver.find_element_by_android_uiautomator('text("SUBMIT")').click()
driver.find_element_by_android_uiautomator('new UiSelector().text("SUBMIT")').click()

driver.back()
time.sleep(5)

"""Option 2nd"""
Contact_us_form = driver.find_element_by_id('com.skill2lead.appiumdemo:id/ContactUs').click()
driver.find_element_by_android_uiautomator('text("Enter Name")').send_keys('Rahul Sharma')
driver.find_element_by_android_uiautomator('text("Enter Email")').send_keys('rahulsharma@zentreelabs.com')
driver.find_element_by_android_uiautomator('text("Enter Address")').send_keys('Bangalore')
driver.find_element_by_android_uiautomator('text("Enter Mobile No")').send_keys('9513645874')
driver.find_element_by_android_uiautomator('text("SUBMIT")').click()

driver.back()

"""Option 3rd"""
wait.until(lambda x : x.find_element_by_id('com.skill2lead.appiumdemo:id/ScrollView')).click()
#driver.find_element_by_id('com.skill2lead.appiumdemo:id/ScrollView').click()
driver.find_element_by_android_uiautomator('UiSelector().index(5)').click()
driver.find_element_by_id('android:id/button2').click()

"""Option 4th"""
wait.until(lambda x: x.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON15"))')).click()
wait.until(lambda x:x.find_element_by_id('android:id/button1')).click()


driver.quit()