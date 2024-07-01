from controller import CalculatorController
from view import CalculatorView

def main():
    view = CalculatorView()
    controller = CalculatorController(view)
    controller.run()

if __name__ == "__main__":
    main()
