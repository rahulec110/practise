import time

import pytest
from Appium_Framework_2.base.DriverClass import Driver

@pytest.fixture(scope='class')
def beforeClass(request):
    print('Before class')
    driver1 = Driver()
    # Now we need to pass this driver object in all the classes for that pytest having 1 parameter called : request
    driver = driver1.getDriverMethod()
    # by using this making a driver object as class level so we have changed the scope as class level
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After class')

@pytest.fixture()
def beforeMethod():
    print('before method')
    yield
    print('after method')