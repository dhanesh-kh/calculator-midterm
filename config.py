import os
import logging.config

# Example environment variable
os.environ['CALCULATOR_MODE'] = 'standard'

def get_calculator_mode():
    return os.getenv('CALCULATOR_MODE', 'standard')

def setup_logging():
    logging.config.fileConfig('logging.conf')