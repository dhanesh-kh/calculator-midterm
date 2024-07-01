"""Contains the logic to handle user input and interaction between model and view"""
import logging
from model import CalculatorModel
from view import CalculatorView

class CalculatorController:
    """handles interactions"""
    def __init__(self, view: CalculatorView):
        self.view = view
        self.model = CalculatorModel()
        self.logger = logging.getLogger('calculator')

    def run(self):
        """run controller"""
        self.logger.info('CalculatorController started.')
        while True:
            try:
                expression = self.view.get_input()
                if expression.lower() == 'exit':
                    self.view.display_message("Exiting the calculator.")
                    self.logger.info('User exited the application.')
                    break
                result = self.model.evaluate_expression(expression)
                self.view.display_result(result)
                self.logger.info('Evaluated expression: %s = %s', expression, result)
            except Exception as e:
                self.view.display_error(f"Error: {e}")
                self.logger.error('Error evaluating expression: %s', e)
