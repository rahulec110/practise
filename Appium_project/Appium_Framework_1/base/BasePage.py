import time
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import Appium_Framework_1.utilities.CustomLogger as cl

class BasePage:
    log = cl.customLogger()
    def __init__(self,driver):
        self.driver = driver
        # we need to pass the driver object to this class so that we can able to call this methods

    def waitForElement(self, locatorValue, locatorType):
        locatorType = locatorType.lower()
        element = 0
        wait = WebDriverWait(self.driver,timeout=20,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,NoSuchElementException])

        if locatorType == 'id':
            element = wait.until(lambda x:x.find_element_by_id(locatorValue))
            return element
        elif locatorType == 'class':
            element = wait.until(lambda x:x.find_element_by_class_name(locatorValue))
            return element
        elif locatorType == 'des':
            element = wait.until(lambda x:x.find_element_by_android_uiautomator('UiSelector().description("%s")'%(locatorValue)))
            return element
        elif locatorType == 'index':
            element = wait.until(lambda x:x.find_element_by_android_uiautomator('UiSelector().index(%d)'%int(locatorValue)))
            return element
        elif locatorType == 'text':
            element = wait.until(lambda x:x.find_element_by_android_uiautomator('text("%s")'%locatorValue))
            return element
        elif locatorType == 'xpath':
            element = wait.until(lambda x:x.find_element_by_xpath('%s'%(locatorValue)))
            return element
        else:
            self.log.info("Locator value " + locatorValue + "not found")
        return element

    def getElement(self,locatorValue, locatorType='id'):
        element = 0
        try:
            locatorType=locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType='id')
            self.log.info('Element found with locator type: '+locatorType+ " and with locator value: "+ locatorValue)
        except:
            self.log.info("Element not found with LocatorType: " + locatorType + " with the locatorValue: " + locatorValue)
        return element

    def clickElement(self,locatorValue, locatorType='id'):
        element = 0
        try:
            locatorType=locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info('Clicked on Element with locator type: '+(locatorType)+ " and with locator value: "+(locatorValue))
        except:
            self.log.info("Unable to click on Element with locator Type "+locatorType+ " and with the locatorvalue."+locatorValue)

    def sendText(self, text, locatorValue, locatorType='id'):
        element = 0
        try:
            locatorType=locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType='id')
            element.send_keys(text)
            self.log.info('Send text on Element with locator type: '+locatorValue+ " and with locator value"+locatorValue)
        except:
            self.log.info('unable to send text on element with locatorType '+locatorType+ " and with locatorValue "+locatorValue)

    def isDisplayed(self,locatorValue, locatorType):
        element = 0
        try:
            locatorType=locatorType.lower()
            element=self.waitForElement(locatorValue,locatorType='id')
            element.is_displayed()
            self.log.info('Element with locatorType '+locatorType+ " and with locatorValue "+locatorValue)
            return True
        except:
            self.log.info('Element with LocatorType: ' + locatorType + ' and with the locatorValue: ' + locatorValue+ ' is not displayed')
            return False

    def screenShot(self,screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path: " + screenshotPath)

        except:
            self.log.info("Unable to save screenshot to the path: " + screenshotPath)

    def scrollElement(self, locatorValue, locatorType):
        element = 0
        try:
            locatorType = locatorType.lower()
            wait = WebDriverWait(self.driver, 25, poll_frequency=1, ignored_exceptions=None)
            element = wait.until(lambda x: x.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(%s("%s"))' % (locatorType, locatorValue)))
            element.click()
        except:
            self.log.info("Unable to scroll")

    def keyCode(self,value):
        self.driver.press_keycode(value)
        self.log.info('Element click with' + value)




