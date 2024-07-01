"""Contains the logic to handle user input and interaction between model and view"""
import logging
from model import CalculatorModel
from view import CalculatorView

class CalculatorController:
    """Handles interactions between model, view, and history"""
    def __init__(self, view: CalculatorView, history):
        self.view = view
        self.history = history  # Assign history object
        self.model = CalculatorModel()  # Assuming CalculatorModel does not require history now
        self.logger = logging.getLogger('calculator')

    def run(self):
        """Starts the controller"""
        self.logger.info('CalculatorController started.')
        while True:
            try:
                expression = self.view.get_input()
                if expression.lower() == 'exit':
                    self.view.display_message("Exiting the calculator.")
                    self.logger.info('User exited the application.')
                    break
                elif expression.lower().startswith('delete '):
                    expression_to_delete = expression[7:]  # Remove 'delete ' prefix
                    self.history.delete_entry(expression_to_delete)
                    self.view.display_message(f"Deleted '{expression_to_delete}' from history.")
                elif expression.lower() == 'clear':
                    self.history.clear_history()
                    self.view.display_message("Cleared history.")
                else:
                    result = self.model.evaluate_expression(expression)
                    if result is not None:
                        self.history.add_entry(expression, result)  # Ensure history is updated on valid expressions
                        self.view.display_result(result)
                        self.logger.info('Evaluated expression: %s = %s', expression, result)
            except Exception as e:
                self.view.display_error(f"Error: {e}")
                self.logger.error('Error evaluating expression: %s', e)





