import pytest

"""To install ordering in pytest: pip3 install pytest-ordering"""

@pytest.mark.run(order= 2)
def test_MethodA():
    print('This is a method A')

@pytest.mark.run(order= 1)
def test_MethodB():
    print('This is a method B')

@pytest.mark.run(order= 4)
def test_MethodC():
    print('This is a method C')

@pytest.mark.run(order= 3)
def test_MethodD():
    print('This is a method D')