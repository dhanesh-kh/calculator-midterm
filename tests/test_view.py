import pytest
from view import CalculatorView
from unittest.mock import patch

@pytest.fixture
def view():
    return CalculatorView()

@patch('builtins.input', return_value='2+3')
def test_get_input(mock_input, view):
    assert view.get_input() == '2+3'

@patch('builtins.print')
def test_display_result(mock_print, view):
    view.display_result(5)
    mock_print.assert_called_with("Result: 5")

@patch('builtins.print')
def test_display_error(mock_print, view):
    view.display_error("Error")
    mock_print.assert_called_with("Error")

@patch('builtins.print')
def test_display_message(mock_print, view):
    view.display_message("Message")
    mock_print.assert_called_with("Message")
