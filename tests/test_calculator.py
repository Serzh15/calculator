from os.path import extsep

import pytest
from calculator import add, subtract, multiply, divide, power, modulo

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 5, 5),
    (-1, -1, -2),
])

def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (0, 0, 0),
    (-1, 1, -2),
])

def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 5, 25),
    (9, 3, 27),
    (1, 2, 2),
])

def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 2),
    (63, 7, 9),
    (22, 2, 11),
])

def test_divide(a, b, expected):
    assert divide(a, b) == expected

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

@pytest.mark.parametrize("a, b, expected", [
    (2,2,4),
    (3,2,9),
    (3,3,27),
    (5,0,1),
    (2,-1,0.5),
    (9.0,0.5,3.0),
])

def test_power(a, b, expected):
    assert power(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10,3,1),
    (5,5,0),
    (9,2,1),
])

def test_modulo(a, b, expected):
    assert modulo(a, b) == expected