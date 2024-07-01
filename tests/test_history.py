# tests/test_history.py
import os
import pandas as pd
import pytest
from calculator.history.calculator_history import CalculatorHistory

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

    # Load test_history.csv using pandas and check if the expression is stored correctly
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'test_history.csv'))
    assert len(df) == 1  # Ensure there is exactly one row in the CSV

    stored_expression = df.iloc[0]['Expression']
    stored_result = df.iloc[0]['Result']

    assert stored_expression == expression
    assert stored_result == result

def test_retrieve_history(history_manager):
    """Test retrieving expression history"""
    # Assuming test_history.csv already contains some entries
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'test_history.csv'))

    # Add more entries to test_history.csv for testing retrieval
    expressions = ["5 * 4", "10 / 2"]
    results = [20.0, 5.0]

    for expr, res in zip(expressions, results):
        history_manager.add_entry(expr, res)

    # Retrieve all entries from history_manager
    history = history_manager.get_history()

    assert len(history) == len(df) + len(expressions)  # Check total number of entries

    for expr, res in zip(expressions, results):
        assert any(entry['Expression'] == expr and entry['Result'] == res for _, entry in history.iterrows())
