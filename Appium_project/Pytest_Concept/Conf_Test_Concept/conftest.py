import pytest

@pytest.fixture(scope='module')
def beforeClass():
    print('Before class')
    yield
    print('After class')

@pytest.fixture()
def beforeMethod():
    print('Befire Method')
    yield
    print('After Method')