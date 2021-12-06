# without confest file
'''from Appium_Framework_2.base.DriverClass import Driver
import Appium_Framework_2.utilities.CustomLogger as cl
from Appium_Framework_2.base.BasePage import BasePage
from Appium_Framework_2.pages.ContactUsPageForm import ContactForm

driver1 = Driver()
log = cl.customLogger()

driver = driver1.getDriverMethod()
cf = ContactForm(driver)

cf.clickContactFormButton()
cf.verifyContactPage()
cf.enterName()
cf.enterEmail()
cf.enterAddress()
cf.enterMNumber()
cf.clickSubmitButton()'''
import unittest
import pytest
from Appium_Framework_2.pages.ContactUsPageForm import ContactForm
import Appium_Framework_2.utilities.CustomLogger as cl

@pytest.mark.usefixtures('beforeClass','beforeMethod') # so that we can use all the features at a time inside this class
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):   # Create the objects for the ContactUsPageForm of the class because to access all the methods
        self.cf = ContactForm(self.driver) # class of ContactUsPageForm
        #to access this object throught out the class we need mention one fixture : @pytest.fixture(autouse=True)
        # so that this object will be available for through out the class.


    @pytest.mark.run(order=2)
    def test_openContactForm(self):
        cl.allureLogs('Filling all the page details...')
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMNumber()
        self.cf.clickSubmitButton()

    @pytest.mark.run(order=1)
    def test_enterDataInForm(self):
        cl.allureLogs('App launching...')
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()




"""rahul@rahul-ThinkPad-P14s-Gen-1:~/PycharmProjects/Appium_project/Appium_Framework_2/tests$ py.test -v -s ContactUsFormTest.py """
"""rahul@rahul-ThinkPad-P14s-Gen-1:~/PycharmProjects/Appium_project/Appium_Framework_2/tests$ 
py.test --alluredir=/home/rahul/PycharmProjects/Appium_project/Appium_Framework_2/reports/allureReports -v -s ContactUsFormTest.py
 
 For report = allure serve /home/rahul/PycharmProjects/Appium_project/Appium_Framework_2/reports/allureReports """


# First of all Create page file under page package
# That page file is working or not so will verify from test file for that page file which are present in Pages package by calling each and every methods.
# Create confest file under test package for using Pytest
# Page file under the test package call the confest file and using fixtures call files under the page.(For Pytest)
# Allure Report : Create allure method in utilities package and import every file where it is required.
