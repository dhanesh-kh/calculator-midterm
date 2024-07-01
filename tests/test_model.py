import pytest
from calculator.model import CalculatorModel

@pytest.fixture
def model():
    return CalculatorModel()

def test_add(model):
    assert model.add(1, 2) == 3

def test_subtract(model):
    assert model.subtract(5, 2) == 3

def test_multiply(model):
    assert model.multiply(3, 4) == 12

def test_divide(model):
    assert model.divide(10, 2) == 5

def test_divide_by_zero(model):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        model.divide(10, 0)

def test_evaluate_expression_add(model):
    assert model.evaluate_expression('10+5') == 15

def test_evaluate_expression_subtract(model):
    assert model.evaluate_expression('10-5') == 5

def test_evaluate_expression_multiply(model):
    assert model.evaluate_expression('10*5') == 50

def test_evaluate_expression_divide(model):
    assert model.evaluate_expression('10/2') == 5

def test_evaluate_expression_invalid_format(model):
    with pytest.raises(ValueError, match="Invalid expression format. Use: <operand1> <operator> <operand2>"):
        model.evaluate_expression('10**2')

def test_evaluate_expression_invalid_operands(model):
    with pytest.raises(ValueError, match="Invalid expression format. Use: <operand1> <operator> <operand2>"):
        model.evaluate_expression('a+b')
