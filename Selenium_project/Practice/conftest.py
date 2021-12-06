import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def init_driver(request):

    web_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    web_driver.maximize_window()
    web_driver.get('https://www.makemytrip.com/flights/')


    yield
    web_driver.close()

    """    web_driver.get('https://zentree.greythr.com/')
        web_driver.find_element(By.ID, 'username').send_keys('ZTL-139')
        time.sleep(2)
        web_driver.find_element(By.ID, 'password').send_keys('Sharma@2014')
        web_driver.find_element(By.XPATH, '//button[text()]').click()
        time.sleep(8)"""