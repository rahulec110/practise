import pytest

# To run all class & module:   "py.test"
# Tu run particular class :
'''1. Go to the particular directory OR run : py.test pytest_package/test_demo1.py
2. py.test test_demo1.py '''
# To run login methd from all the class then run : py.test -k login -v
# -k :is a identifier which test the uniques methods (just like group)
# -v :for more information on console

# to run all login marker method from all classes: py.test -m login
#
@pytest.mark.login
def test_m1():
    a = 3
    b = 4
    assert  a+1 == b, "test failed"
    assert  a==b, "test failed as a is not equal to b"

def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM"
@pytest.mark.login
def test_m3():
    assert True

def test_m4():
    assert False
@pytest.mark.login
def test_m5():
    assert 100 == 100

def test_m6():
    assert "naveen" == "NAVEEN"
@pytest.mark.login
def test_login_FB():
    assert "admin" == "admin123"