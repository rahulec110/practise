import time
import unittest
import pytest

from Appium_Framework_2.base.BasePage import BasePage
from Appium_Framework_2.pages.LoginPage import LoginPageTest
import Appium_Framework_2.utilities.CustomLogger as cl


@pytest.mark.usefixtures('beforeClass','beforeMethod')
class LoginTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.gt = LoginPageTest(self.driver)
        self.bp = BasePage(self.driver)

#    @pytest.mark.run(order=3)
 #   def test_enterDataInEditBox(self):
 #       cl.allureLogs("page is displayed")
 #       self.gt.enterText()
#        self.gt.clickOnSubmit()

    @pytest.mark.run(order=4)
    def test_openLoginScreen(self):
        cl.allureLogs("relaunching app")
        self.bp.keyCode(4)
        self.gt.clickLoginButton()
        self.gt.enterEmail()
        self.gt.enterPassword()
        self.gt.clickLoginB()
        time.sleep(5)
        self.gt.enterText()
        self.gt.clickOnSubmit()
       # self.gt.verifyAdminScreen()


    @pytest.mark.run(order=3)
    def test_loginFailMethod(self):
        cl.allureLogs("Opening app")
        self.gt.clickLoginButton()
        self.gt.enterEmail()
        self.gt.enterPassword2()
        self.gt.clickLoginB()
        self.gt.verifyAdminScreen()
