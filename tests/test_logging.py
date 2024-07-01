"""test logging functionality"""
import os
import logging
import pytest
from calculator.config import setup_logging

@pytest.fixture
def log_file():
    """specify log file"""
    return 'calculator.log'

def test_log_file_creation(log_file):
    """test that log file is created"""
    if os.path.exists(log_file):
        os.remove(log_file)
    setup_logging()
    logger = logging.getLogger('calculator')
    logger.info('Test log message')
    assert os.path.exists(log_file)

def test_log_content(log_file):
    """test log content"""
    setup_logging()
    logger = logging.getLogger('calculator')
    logger.info('Test log message')
    with open(log_file, 'r') as f:
        log_content = f.read()
    assert 'Test log message' in log_content
