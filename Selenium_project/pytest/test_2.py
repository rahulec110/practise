import pytest

def test_m4():
    assert False

@pytest.mark.login
def test_m5():
    assert 100==100

def test_m6():
    assert 'naveen' == 'Naveen'

@pytest.mark.login
def test_login():
    assert 'admin' == 'admin'