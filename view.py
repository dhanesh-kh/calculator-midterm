"""presentation for user interaction"""
import logging

class CalculatorView:
    """functions for user interaction"""
    def __init__(self):
        self.logger = logging.getLogger('calculator')

    def get_input(self) -> str:
        """expression input prompt"""
        expression = input("Enter expression (or type 'exit' to quit): ")
        self.logger.debug('User input: %s', expression)
        return expression

    def display_result(self, result: float):
        """result prompt"""
        print(f"Result: {result}")
        self.logger.debug('Displayed result: %s', result)

    def display_error(self, message: str):
        """error prompt"""
        print(message)
        self.logger.error('Displayed error: %s', message)

    def display_message(self, message: str):
        """message prompt"""
        print(message)
        self.logger.info('Displayed message: %s', message)
