import pytest

def test_should_pass_str():
    assert "a" == "a"
 
@pytest.mark.skip(reason="skip")
def test_should_fail_str():
    assert "a" != "a"
