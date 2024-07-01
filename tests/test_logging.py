# test_logging.py
import os
import logging
import pytest
from calculator.config import setup_logging

@pytest.fixture
def log_file():
    """Specify log file"""
    return 'logs/calculator.log'  # Update to match the new log file location

def setup_module():
    """Setup logging for tests"""
    setup_logging()

def test_log_file_creation(log_file):
    """Test that log file is created"""
    if os.path.exists(log_file):
        os.remove(log_file)
    logger = logging.getLogger('calculator')
    logger.info('Test log message')
    assert os.path.exists(log_file)

def test_log_content(log_file):
    """Test log content"""
    logger = logging.getLogger('calculator')
    logger.info('Test log message')
    with open(log_file, 'r') as f:
        log_content = f.read()
    assert 'Test log message' in log_content
