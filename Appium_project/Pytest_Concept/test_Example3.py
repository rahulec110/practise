import pytest

@pytest.fixture()
def setUp():
    '''We can keep any name here instead of setUp'''
    print('Before a Method')

def test_methodA(setUp):
    print("This is method A")

def test_methodB(setUp):
    print("This is method B")
