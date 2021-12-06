'''To run your test cases in parallel mode, you need to install pytest-xdist package.
pip install pytest-xdist'''
#  rahul@rahul-ThinkPad-P14s-Gen-1:~/PycharmProjects/Selenium_project$ py.test pytest_package/test_webpage_login.py
# Run for parallel mode :  py.test pytest_package/test_webpage_login.py -n 5


from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(4)
    driver.get('http://www.google.com')
    assert driver.title == 'Google'
    time.sleep(2)
    driver.close()

def test_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(4)
    driver.get('http://www.facebook.com')
    #assert driver.title == 'Facebook – log in or sign up'
    assert driver.title == 'लॉग इन या साइन अप करें'
    time.sleep(2)
    driver.close()

def test_Instagram():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(4)
    driver.get('http://www.instagram.com')
    assert driver.title == 'Instagram'
    time.sleep(2)
    driver.close()

def test_gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(4)
    driver.get('http://www.gmail.com')
    assert driver.title == 'Gmail'
    time.sleep(2)
    driver.close()

def test_rediff():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(4)
    driver.get('http://www.rediff.com')
    assert driver.title == 'Rediff.com: News | Rediffmail | Stock Quotes | Shopping'
    time.sleep(2)
    driver.close()