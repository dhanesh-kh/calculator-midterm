# config.py
import os
import logging.config

# Ensure the logs directory exists
logs_dir = 'logs'
os.makedirs(logs_dir, exist_ok=True)

# Example environment variable
os.environ['CALCULATOR_MODE'] = 'standard'

def get_calculator_mode():
    """Setup environment variables"""
    return os.getenv('CALCULATOR_MODE', 'standard')

def setup_logging():
    """Setup logging"""
    logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
