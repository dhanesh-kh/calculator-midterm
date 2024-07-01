import re
import logging

class CalculatorModel:
    def __init__(self):
        self.logger = logging.getLogger('calculator')

    def add(self, a: float, b: float) -> float:
        self.logger.debug('Adding: %s + %s', a, b)
        return a + b

    def subtract(self, a: float, b: float) -> float:
        self.logger.debug('Subtracting: %s - %s', a, b)
        return a - b

    def multiply(self, a: float, b: float) -> float:
        self.logger.debug('Multiplying: %s * %s', a, b)
        return a * b

    def divide(self, a: float, b: float) -> float:
        self.logger.debug('Dividing: %s / %s', a, b)
        if b == 0:
            self.logger.error('Division by zero attempted.')
            raise ValueError("Cannot divide by zero.")
        return a / b

    def evaluate_expression(self, expression: str) -> float:
        self.logger.debug('Evaluating expression: %s', expression)
        match = re.fullmatch(r'(\d+\.?\d*)([+\-*/])(\d+\.?\d*)', expression.replace(' ', ''))
        if not match:
            self.logger.error('Invalid expression format: %s', expression)
            raise ValueError("Invalid expression format. Use: <operand1> <operator> <operand2>")

        operand1, operator, operand2 = match.groups()

        try:
            operand1 = float(operand1)
            operand2 = float(operand2)
        except ValueError:
            self.logger.error('Operands must be numbers: %s, %s', operand1, operand2)
            raise ValueError("Operands must be numbers.")

        if operator == '+':
            return self.add(operand1, operand2)
        elif operator == '-':
            return self.subtract(operand1, operand2)
        elif operator == '*':
            return self.multiply(operand1, operand2)
        elif operator == '/':
            return self.divide(operand1, operand2)
        else:
            self.logger.error('Unsupported operator: %s', operator)
            raise ValueError("Unsupported operator. Use +, -, *, or /.")
