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
    result = add(
        multiply(2,4), 2
    ), divide(5,0),
    subtract(1,1)
    assert result == ValueError("Divide by zero")