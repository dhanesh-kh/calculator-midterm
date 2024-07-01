# tests/test_history.py
import os
import pandas as pd
import pytest
from history.calculator_history import CalculatorHistory

@pytest.fixture(scope="module")
def setup_history_file():
    """Fixture to ensure test_history.csv exists and is empty before tests."""
    filename = os.path.join(os.path.dirname(__file__), 'test_history.csv')
    if os.path.exists(filename):
        os.remove(filename)
    df = pd.DataFrame(columns=['Expression', 'Result'])  # Initialize empty DataFrame
    df.to_csv(filename, index=False)

@pytest.fixture
def history_manager(setup_history_file):
    """Fixture to initialize CalculatorHistory"""
    return CalculatorHistory(filename=os.path.join(os.path.dirname(__file__), 'test_history.csv'))

def test_store_expression(history_manager):
    """Test storing an expression"""
    expression = "2 + 3"
    result = 5.0  # Assuming the result of the expression
    history_manager.add_entry(expression, result)

    # Retrieve all entries from history_manager
    history = history_manager.get_history()

    assert len(history) == 1  # Ensure there is exactly one entry
    assert history.iloc[0]['Expression'] == expression
    assert history.iloc[0]['Result'] == result

def test_retrieve_history(history_manager):
    """Test retrieving expression history"""
    expressions = ["5 * 4", "10 / 2"]
    results = [20.0, 5.0]

    for expr, res in zip(expressions, results):
        history_manager.add_entry(expr, res)

    # Retrieve all entries from history_manager
    history = history_manager.get_history()

    expected_entries = len(expressions) + 1  # Initial entry plus new entries
    assert len(history) == expected_entries

    for expr, res in zip(expressions, results):
        assert any((history['Expression'] == expr) & (history['Result'] == res))



