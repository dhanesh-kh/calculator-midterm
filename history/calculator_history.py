# history/calculator_history.py
import pandas as pd
import os
import logging

class CalculatorHistory:
    def __init__(self, filename='history.csv'):
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.logger = logging.getLogger('calculator.history')
        self.logger.setLevel(logging.DEBUG)  # Set log level to DEBUG
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        self.history = pd.DataFrame(columns=['Expression', 'Result'])
        self.load_history()

    def load_history(self):
        try:
            self.history = pd.read_csv(self.filename)
            self.logger.debug('Loaded history from file: %s', self.filename)
        except FileNotFoundError:
            self.logger.warning('History file not found: %s', self.filename)
            self.history = pd.DataFrame(columns=['Expression', 'Result'])  # Initialize empty if not found
            self.history.to_csv(self.filename, index=False)
            self.logger.debug('Created new history file: %s', self.filename)

    def add_entry(self, expression, result):
        entry = pd.DataFrame({'Expression': [expression], 'Result': [result]})
        self.history = pd.concat([self.history, entry], ignore_index=True)
        self.history.to_csv(self.filename, index=False)
        self.logger.debug('Added entry to history: %s = %s', expression, result)

    def get_history(self):
        return self.history
