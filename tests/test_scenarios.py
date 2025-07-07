import pytest
from calculator import add, multiply, subtract, power, divide

def test_complex_expression():
    result = subtract(
        multiply(
            add(2,3), 4
        ),
            power(5,2)
        )
    assert result == -5

def test_complex_exp_fail():
    with pytest.raises(ZeroDivisionError):
        result = subtract(
            add(multiply(2,4), divide(5,0)),
            1
        )