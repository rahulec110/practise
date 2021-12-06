from Appium_Framework_2.base.BasePage import BasePage
import Appium_Framework_2.utilities.CustomLogger as cl

class LoginPageTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in login Page
    _loginButton = "com.skill2lead.appiumdemo:id/Login" #id
    _enterEmail = "3"  #index
    _enterPassword = "Enter Password" #text
    _click_Login = "com.skill2lead.appiumdemo:id/Btn3" #id
    _wrongCredentila = "Wrong Credentials" #text
    _pageTitle = "Enter Admin" #text
    _enterText = "com.skill2lead.appiumdemo:id/Edt_admin"  # id
    _submitButton = "SUBMIT"  # text


    def clickLoginButton(self):
        self.clickElement(self._loginButton,"id")
        cl.allureLogs("Click on login Button")

    def enterEmail(self):
        self.sendText("admin@gmail.com",self._enterEmail,"index")
        cl.allureLogs("entered email id")

    def enterPassword(self):
        self.sendText("admin123",self._enterPassword,"text")
        cl.allureLogs("entered password")

    def enterPassword2(self):
        self.sendText("admin1234",self._enterPassword,"text")
        cl.allureLogs("entered password")

    def clickLoginB(self):
        self.clickElement(self._click_Login,"id")
        cl.allureLogs("lciked on login button in login screen")

    def verifyAdminScreen(self):
        adminScreen = self.isDisplayed(self._pageTitle,"text")
        assert adminScreen == True
        cl.allureLogs("Opened admin screen")

    def enterText(self):
        self.sendText("Code2Lead",self._enterText,"id")
        cl.allureLogs("Entered Text")

    def clickOnSubmit(self):
        self.clickElement(self._submitButton,"text")
        cl.allureLogs("Clicked on Submit Button")


