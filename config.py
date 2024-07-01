"""config file for logging and env variables"""
import os
import logging.config

# Example environment variable
os.environ['CALCULATOR_MODE'] = 'standard'

def get_calculator_mode():
    """setup environment variables"""
    return os.getenv('CALCULATOR_MODE', 'standard')

def setup_logging():
    """setup logging"""
    logging.config.fileConfig('logging.conf')
