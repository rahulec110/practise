''' pytest -v -s pytest_package/test_google_test.py '''
'''For html report need to install package:  pip install pytest-html'''
'''run with html report:  pytest pytest_package/test_google_test.py -v -s --html=google_test_report.html'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time
import pytest

driver = None

def setup_module(module):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('http://www.google.com')

def teardown_module(module):

    time.sleep(3)
    driver.quit()

def test_google_title():
    assert driver.title == 'Google'

def test_google_url():
    assert driver.current_url == 'https://www.google.com/?gws_rd=ssl'

