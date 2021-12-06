import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

'''To run : pytest test_6_fixture_module.py -v --html=report.html 
By using the fixture we can set the scope as module/class    : @pytest.fixture(scope='module')
we have 2 choices, either we write the fixture name inside the bracket of test method or we can write 1 anotation before the mathod:
@pytest.mark.usefixtures('init_driver')'''

driver = None
@pytest.fixture(scope='module')
def init_driver():
    global driver
    print('---------------setup------------------')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('http://www.google.com')

    yield
    print('---------------Tear down----------------')
    driver.quit()

@pytest.mark.usefixtures('init_driver')
def test_google_title():
    assert driver.title == 'Google'

@pytest.mark.usefixtures('init_driver')
def test_google_url():
    assert driver.current_url == 'https://www.google.com/?gws_rd=ssl'