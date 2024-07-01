import pytest
from controller import CalculatorController
from view import CalculatorView
from unittest.mock import Mock

@pytest.fixture
def view():
    return Mock(spec=CalculatorView)

@pytest.fixture
def controller(view):
    return CalculatorController(view)

def test_run_exit(controller, view):
    view.get_input.side_effect = ['exit']
    controller.run()
    view.display_message.assert_called_with("Exiting the calculator.")

def test_run_addition(controller, view):
    view.get_input.side_effect = ['2+3', 'exit']
    controller.run()
    view.display_result.assert_called_with(5.0)
