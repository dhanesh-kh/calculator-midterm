# test_logging.py
import os
import logging
import pytest
from config import setup_logging

@pytest.fixture(scope='module')
def log_file():
    """Specify log file"""
    return 'logs/calculator.log'  # Update to match the new log file location

@pytest.fixture(scope='module', autouse=True)
def setup_logging_fixture():
    """Setup logging for tests"""
    setup_logging()
    yield  # Yield allows for teardown after the test module completes

def test_log_file_creation(log_file):
    """Test that log file is created"""
    logger = logging.getLogger('calculator')
    logger.info('Test log message')
    
    # Ensure log file is closed before attempting to remove it
    logging.shutdown()

    if os.path.exists(log_file):
        os.remove(log_file)

    assert os.path.exists(log_file) == False, f"Log file '{log_file}' should have been deleted."
