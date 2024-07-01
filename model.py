# model.py
import re
import logging
from history.calculator_history import CalculatorHistory

class CalculatorModel:
    """Manages calculator logic"""
    def __init__(self):
        self.logger = logging.getLogger('calculator')
        self.logger.setLevel(logging.DEBUG)  # Set log level to DEBUG
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
        self.history_manager = CalculatorHistory()

    def add(self, a: float, b: float) -> float:
        """Addition function"""
        self.logger.debug('Adding: %s + %s', a, b)
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtraction function"""
        self.logger.debug('Subtracting: %s - %s', a, b)
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiplication function"""
        self.logger.debug('Multiplying: %s * %s', a, b)
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Division function"""
        self.logger.debug('Dividing: %s / %s', a, b)
        if b == 0:
            self.logger.error('Division by zero attempted.')
            raise ValueError("Cannot divide by zero.")
        return a / b

    def evaluate_expression(self, expression: str) -> float:
        """Evaluate given expression"""
        self.logger.debug('Evaluating expression: %s', expression)
        
        # Validate expression format
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

        # Evaluate based on operator
        if operator == '+':
            result = self.add(operand1, operand2)
        elif operator == '-':
            result = self.subtract(operand1, operand2)
        elif operator == '*':
            result = self.multiply(operand1, operand2)
        elif operator == '/':
            result = self.divide(operand1, operand2)
        else:
            self.logger.error('Unsupported operator: %s', operator)
            raise ValueError("Unsupported operator. Use +, -, *, or /.")

        # Add entry to history
        self.history_manager.add_entry(expression, result)

        return result

    def get_history(self):
        """Retrieve expression history"""
        return self.history_manager.get_history()
