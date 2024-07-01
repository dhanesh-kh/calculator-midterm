"""tests for controller"""
from unittest.mock import Mock
import pytest
from controller import CalculatorController
from view import CalculatorView


@pytest.fixture
def view():
    """test view"""
    return Mock(spec=CalculatorView)

@pytest.fixture
def controller(view):
    """test controller"""
    return CalculatorController(view)

def test_run_exit(controller, view):
    """test exit"""
    view.get_input.side_effect = ['exit']
    controller.run()
    view.display_message.assert_called_with("Exiting the calculator.")

def test_run_addition(controller, view):
    """test addition"""
    view.get_input.side_effect = ['2+3', 'exit']
    controller.run()
    view.display_result.assert_called_with(5.0)
