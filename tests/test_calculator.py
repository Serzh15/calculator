import pytest
from calculator.calculator import add, subtract, multiply, divide

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 5, 5),
    (-1, -1, -2),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

def test_sub(a, b, expected):
    assert subtract(a, b) == expected

def test_mult(a, b, expected):
    assert multiply(a, b) == expected

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
