from model import CalculatorModel
from view import CalculatorView

class CalculatorController:
    def __init__(self, view: CalculatorView):
        self.view = view
        self.model = CalculatorModel()

    def run(self):
        while True:
            try:
                expression = self.view.get_input()
                if expression.lower() == 'exit':
                    self.view.display_message("Exiting the calculator.")
                    break
                result = self.model.evaluate_expression(expression)
                self.view.display_result(result)
            except Exception as e:
                self.view.display_error(f"Error: {e}")

