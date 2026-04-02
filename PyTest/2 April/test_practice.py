import pytest

def test_change():
    assert "hello" == "hello", 'Not Equal'
    assert 5 == 5, 'Not Equal'


def test_comparison():
    assert 45 >= 33, "Not greater than"


def test_membership():
    l = [1, 2, 3]
    assert 3 in l, 'Not in the list'


@pytest.skip(reason="Skipping this test for demo")
def test_change():
    assert "hello" == "hello", 'Not Equal'
    assert 5 == 5, 'Not Equal'


@pytest.mark.skipif(2 > 1, reason="Condition is true so skipping")
def test_comparison():
    assert 45 >= 33, "Not greater than"

@pytest.mark.parametrize("value", [1, 2, 3])
def test_membership(value):
    l = [1, 2, 3]
    assert value in l, 'Not in the list'

