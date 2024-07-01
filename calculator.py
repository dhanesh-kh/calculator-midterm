"""Calculator application entry point"""
import logging
import logging.config
import os

from controller import CalculatorController
from view import CalculatorView
from history.calculator_history import CalculatorHistory

def setup_logging(default_path='logging.conf', default_level=logging.INFO):
    """Setup logging configuration"""
    if os.path.exists(default_path):
        logging.config.fileConfig(default_path)
    else:
        logging.basicConfig(level=default_level)

def main():
    """Start application and logging"""
    setup_logging()
    logger = logging.getLogger('calculator')
    logger.info('Starting Calculator Application')

    view = CalculatorView()
    history = CalculatorHistory()  # Initialize CalculatorHistory instance
    controller = CalculatorController(view, history)  # Pass history to CalculatorController

    try:
        controller.run()
    except Exception as e:
        logger.exception('An unexpected error occurred: %s', e)

if __name__ == "__main__":
    main()

