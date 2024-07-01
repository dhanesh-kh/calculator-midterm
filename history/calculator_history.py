# history/calculator_history.py
import pandas as pd
import os
import logging

class CalculatorHistory:
    def __init__(self, filename='history.csv'):
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.logger = logging.getLogger('calculator.history')
        self.logger.setLevel(logging.DEBUG)  # Set log level to DEBUG

        # Configure logging handler only once
        if not self.logger.hasHandlers():
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
        # Check if the entry already exists in history to prevent duplicates
        if not self.history[(self.history['Expression'] == expression) & (self.history['Result'] == result)].empty:
            self.logger.debug('Entry already exists in history: %s = %s', expression, result)
            return

        # Ensure the entry is valid
        if expression and result is not None:
            entry = pd.DataFrame({'Expression': [expression], 'Result': [result]})

            # Exclude empty or all-NA columns from the entry before concatenation
            if not entry.dropna(axis=1, how='all').empty:
                self.history = pd.concat([self.history, entry], ignore_index=True)
                self.history.to_csv(self.filename, index=False)
                self.logger.debug('Added entry to history: %s = %s', expression, result)
            else:
                self.logger.warning('Attempted to add empty or all-NA entry: %s = %s', expression, result)
        else:
            self.logger.warning('Attempted to add invalid entry: %s = %s', expression, result)

    def get_history(self):
        return self.history


