# import the files

import unittest
from Appium_Framework_2.tests.loginTest import LoginTest
from Appium_Framework_2.tests.ContactUsFormTest import ContactFormTest

# 2. Create the object of the class unsing unittest

cf = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)
gt = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# 3. create TestSuite
regressionTest = unittest.TestSuite([cf,gt])

#4. Call the Test Runner method

unittest.TextTestRunner(verbosity=1).run(regressionTest)
