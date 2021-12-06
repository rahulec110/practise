import time

from appium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'OnePlus Nord'
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'org.chromium.chrome.browser.ChromeTabbedActivity'

# 1. Create the Driver object
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 2. Create WebDriverWait
wait = WebDriverWait(driver, 25, poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,NoSuchElementException])

# 3. Open the URL in Browser
ele = wait.until(lambda x: x.find_element_by_id("com.android.chrome:id/terms_accept"))
ele.click()

ele2 = wait.until(lambda x: x.find_element_by_id("com.android.chrome:id/next_button"))
ele2.click()

ele3 = wait.until(lambda x: x.find_element_by_id("com.android.chrome:id/negative_button"))
ele3.click()

ele4 = wait.until(lambda x: x.find_element_by_id("com.android.chrome:id/search_box_text"))
ele4.click()

ele5 = wait.until(lambda x: x.find_element_by_id("com.android.chrome:id/url_bar"))
ele5.click()
ele5.send_keys("http://www.dummypoint.com/")
# to enter
driver.press_keycode(66)
time.sleep(5)

# 4. Get the list of Contexts in App
appContexts = driver.contexts
print("AppContexts : ", appContexts)


# 5. switch to webview to perform action on Required URL or on WebView
for appType in appContexts:
    if appType == "WEBVIEW_chrome":
        print("In WebView")
        driver.switch_to.context(appType)

# 6. Do testing on Webview screen in chrome browser or any if we want
enterText = wait.until(lambda x: x.find_element_by_link_text("fas fa-search"))
#enterText = wait.until(lambda x: x.find_element_by_class_name('nav-link nav-link-lg d-sm-none'))
enterText.click()
enterText.send_keys("Code2Lead")

'''/tmp/.mount_AppiumqJ1xcx/resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/linux/chromedriver_64'''