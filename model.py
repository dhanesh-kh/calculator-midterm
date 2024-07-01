class CalculatorModel:
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def evaluate_expression(self, expression: str) -> float:
        tokens = expression.split()
        if len(tokens) != 3:
            raise ValueError("Invalid expression format. Use: <operand1> <operator> <operand2>")

        operand1, operator, operand2 = tokens
        try:
            operand1 = float(operand1)
            operand2 = float(operand2)
        except ValueError:
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
            raise ValueError("Unsupported operator. Use +, -, *, or /.")
