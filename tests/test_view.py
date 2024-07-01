"""test for prompts"""
from unittest.mock import patch
import pytest
from view import CalculatorView

@pytest.fixture
def view():
    """view"""
    return CalculatorView()

@patch('builtins.input', return_value='2+3')
def test_get_input(mock_input, view):
    """test input"""
    assert view.get_input() == '2+3'

@patch('builtins.print')
def test_display_result(mock_print, view):
    """test result"""
    view.display_result(5)
    mock_print.assert_called_with("Result: 5")

@patch('builtins.print')
def test_display_error(mock_print, view):
    """test error"""
    view.display_error("Error")
    mock_print.assert_called_with("Error")

@patch('builtins.print')
def test_display_message(mock_print, view):
    """test message"""
    view.display_message("Message")
    mock_print.assert_called_with("Message")
