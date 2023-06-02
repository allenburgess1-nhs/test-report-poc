import pytest

def test_should_pass_add():
    assert 1 + 1 == 2

def test_should_pass_minus():
    assert 2 - 1 == 1
    
def test_should_pass_multiply():
    assert 2 * 2 == 4

@pytest.mark.skip(reason="skip")
def test_should_fail_add():
    assert 1 + 1 == 3
