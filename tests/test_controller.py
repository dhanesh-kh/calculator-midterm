"""tests for controller"""
from unittest.mock import Mock
import pytest
from controller import CalculatorController
from view import CalculatorView
from history.calculator_history import CalculatorHistory

@pytest.fixture
def view():
    """Fixture for mock view"""
    return Mock(spec=CalculatorView)

@pytest.fixture
def history():
    """Fixture for mock history"""
    return Mock(spec=CalculatorHistory)

@pytest.fixture
def controller(view, history):
    """Fixture for calculator controller with mock view and history"""
    return CalculatorController(view, history)

def test_run_exit(controller, view):
    """Test exit command"""
    view.get_input.side_effect = ['exit']
    controller.run()
    view.display_message.assert_called_with("Exiting the calculator.")

def test_run_addition(controller, view):
    """Test addition command"""
    view.get_input.side_effect = ['2+3', 'exit']
    controller.run()
    view.display_result.assert_called_with(5.0)

def test_clear_history(controller, view, history):
    """Test clear history command"""
    view.get_input.side_effect = ['clear', 'exit']
    controller.run()
    history.clear_history.assert_called_once()
    view.display_message.assert_any_call("Cleared history.")

def test_delete_expression(controller, view, history):
    """Test delete expression command"""
    view.get_input.side_effect = ['delete 2+3', 'exit']
    controller.run()
    history.delete_entry.assert_called_once_with('2+3')
    view.display_message.assert_any_call("Deleted '2+3' from history.")


