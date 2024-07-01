import os

# Example environment variable
os.environ['CALCULATOR_MODE'] = 'standard'

def get_calculator_mode():
    return os.getenv('CALCULATOR_MODE', 'standard')
