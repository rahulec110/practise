import pytest

def test_methodA():
    print('This is methos A')

def test_methodB():
    print('This is method B')
@pytest.mark.skip
def test_methodC():
    print("This is method C")

def test_methodD():
    print("This is method D")

'''
Run Allure command:
  >> py.test --alluredir='/home/rahul/Allure_report/Appium_Python_logs' -v -s test_pytestAllure.py 

To create Report:
  >> To generate test suit: allure serve /home/rahul/Allure_report/Appium_Python_logs
'''