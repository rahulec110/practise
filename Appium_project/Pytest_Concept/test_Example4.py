import pytest

'''Example for before method and after method'''

@pytest.fixture()
def setUp():
    print('Before a method')
    yield
    print('After a method')

def test_methodA(setUp):
    print("This is method A")

def test_methodB(setUp):
    print("This is method B")