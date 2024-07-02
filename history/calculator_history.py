"""history/calculator_history.py"""
import os
import logging
import pandas as pd

class CalculatorHistory:
    """Handle expression history using pandas"""
    def __init__(self, filename='history.csv'):
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.logger = logging.getLogger('calculator.history')
        self.logger.setLevel(logging.DEBUG)  # Set log level to DEBUG

        if not self.logger.hasHandlers():
            # Add only the file handler
            handler = logging.FileHandler('logs/calculator.log', 'a')
            handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

            # Check if log file exists, log creation if it doesn't
            log_file = 'logs/calculator.log'
            if not os.path.exists(log_file):
                self.logger.info('Created new log file: %s', log_file)

        self.history = pd.DataFrame(columns=['Expression', 'Result'])
        self.load_history()

    def load_history(self):
        """Load history from file or create one if none is found"""
        try:
            self.history = pd.read_csv(self.filename)
            self.logger.debug('Loaded history from file: %s', self.filename)
        except FileNotFoundError:
            self.logger.warning('History file not found: %s', self.filename)
            self.history = pd.DataFrame(columns=['Expression', 'Result'])
            self.history.to_csv(self.filename, index=False)
            self.logger.debug('Created new history file: %s', self.filename)

    def add_entry(self, expression, result):
        """Add an entry to history file"""
        if expression and result is not None:
            entry = pd.DataFrame({'Expression': [expression], 'Result': [result]})
            if not entry.dropna(axis=1, how='all').empty:
                self.history = pd.concat([self.history, entry], ignore_index=True)
                self.history.to_csv(self.filename, index=False)
                self.logger.debug('Added entry to history: %s = %s', expression, result)
            else:
                self.logger.warning('Attempted to add empty or all-NA entry: %s = %s', expression, result)
        else:
            self.logger.warning('Attempted to add invalid entry: %s = %s', expression, result)

    def clear_history(self):
        """Clear all history entries"""
        self.history = pd.DataFrame(columns=['Expression', 'Result'])
        self.history.to_csv(self.filename, index=False)
        self.logger.info('Cleared history.')

    def delete_entry(self, expression):
        """Delete a specific expression from history"""
        if expression in self.history['Expression'].values:
            self.history = self.history[self.history['Expression'] != expression]
            self.history.to_csv(self.filename, index=False)
            self.logger.info('Deleted expression from history: %s', expression)
        else:
            self.logger.warning('Expression not found in history: %s', expression)

    def get_history(self):
        """Return history DataFrame"""
        return self.history
