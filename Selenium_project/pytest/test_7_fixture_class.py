#   pytest -v -s test_7_fixture_class.py
#   pytest test_7_fixture_class.py - v - s - -html = report.html
#   pytest test_7_fixture_class.py -v -s -n 2 --html=report.html

'''if i am not defining global driver variable then we can resolve this problem by craete a parameter under the method:
     def init_driver(request):
         web_driver = webdriver.Chrome(ChromeDriverManager().install())
         request.cls.driver = web_driver

         yield
         web_driver.close()
          >> As a class level using driver variable to access web webdriver'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest

@pytest.fixture(params=['chrome','firefox'],scope='class')
def init_driver(request):
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == 'firefox':
        web_driver = webdriver.Firefox(executable_path = GeckoDriverManager().install())
    request.cls.driver = web_driver

    yield
    web_driver.close()

@pytest.mark.usefixtures('init_driver')
class BaseTest:
    pass

class Test_Google(BaseTest):

    def test_google_title(self):
        self.driver.get('http://www.google.com')
        assert self.driver.title == 'Google'

    def test_google_Url(self):
        self.driver.get('http://www.google.com')
        assert self.driver.current_url == 'https://www.google.com/'

