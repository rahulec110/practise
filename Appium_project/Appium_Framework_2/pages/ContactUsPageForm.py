from Appium_Framework_2.base.BasePage import BasePage
import Appium_Framework_2.utilities.CustomLogger as cl

class ContactForm(BasePage):
# creted initialization method because we need to pass driver object to this class so that we call all the methods.
    def __init__(self, driver):
        super().__init__(driver) # Override the parent initialization method becase Base page also having initialization method so that overriding here.
        self.driver = driver

    # Locators values in Contact us form
    _contactFromButton = "com.skill2lead.appiumdemo:id/ContactUs"  # id
    _pagetitle = "Contact Us form"  # text
    _enterName = "Enter Name"  # text
    _enterEmail = "Enter Email"  # text
    _enterAddress = "Enter Address"  # text
    _enterMobileNumber = "4"  # index number
    _submitButton = "SUBMIT"  # text

    def clickContactFormButton(self):
        self.clickElement(self._contactFromButton, "id")
        cl.allureLogs("Clicked on Contact us form button")# calling the method for allure logs

    def verifyContactPage(self):
        element = self.isDisplayed(self._pagetitle, "text")
        assert element == True
        cl.allureLogs("Contact Us Form page opened")

    def enterName(self):
        self.sendText("Code2Lead",self._enterName,"text")
        cl.allureLogs("Entered Name details")

    def enterEmail(self):
        self.sendText("abc@gmail.com",self._enterEmail,"text")
        cl.allureLogs("Entered Email address")

    def enterAddress(self):
        self.sendText("India",self._enterAddress,"text")
        cl.allureLogs("Entered Address of the User")

    def enterMNumber(self):
        self.sendText("987654210",self._enterMobileNumber, "index")
        # Intensially failing this case for screenshot in allure
        #self.sendText("987654210","ABX","index")
        cl.allureLogs("Entered Mobile number")

    def clickSubmitButton(self):
        self.clickElement(self._submitButton,"text")
        cl.allureLogs("Clicked on Submit button")