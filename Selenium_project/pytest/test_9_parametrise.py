import time

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('init_driver')
class Test:
    pass

class Test_GreyIt(Test):
    @pytest.mark.parametrize(
                               "username, password",
                                 [
                                     ('ZTL-139', 'Sharma@2014'),
                                 ]
                             )
    def test_login(self,username, password):

        self.driver.get('https://zentree.greythr.com/')
        self.driver.find_element(By.ID,'username').send_keys(username)
        time.sleep(2)
        self.driver.find_element(By.ID,'password').send_keys(password)
        self.driver.find_element(By.XPATH, '//button[text()]').click()
        time.sleep(8)
