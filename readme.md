## Calculator Application
This project is a command-line calculator application in Python, focused on data handling, logging, environment variables, and error handling.

### Design Patterns
Some design patterns used in the project:

- Model-View-Controller (MVC): Separates the application into three interconnected components to separate internal representations of information from the ways that information is presented and accepted.
    - [model.py](https://github.com/dhanesh-kh/calculator-midterm/blob/master/model.py)
    - [view.py](https://github.com/dhanesh-kh/calculator-midterm/blob/master/view.py)
    - [controller.py](https://github.com/dhanesh-kh/calculator-midterm/blob/master/controller.py)
- Singleton: Used in `CalculatorHistory` to ensure there's only one instance handling expression history.
    - [calculator_history.py](https://github.com/dhanesh-kh/calculator-midterm/blob/master/history/calculator_history.py)

### Environment Variables
Environment variables are used to configure aspects of the application such as logging levels, operational modes and history file name.

- Configuration: Managed through `config.py`, which loads environment variables from `.env` and configures application behavior.
    - [config.py](https://github.com/dhanesh-kh/calculator-midterm/blob/master/config.py)
    - [conftest.py](https://github.com/dhanesh-kh/calculator-midterm/blob/master/tests/conftest.py)
    - setting `history_file` and `log_level` in [calculator_history.py](https://github.com/dhanesh-kh/calculator-midterm/blob/master/history/calculator_history.py)

### Logging
Logging is configured using `logging.conf`, ensuring detailed output for debugging and operational insights.

- Logging Setup: Initialized in `calculator.py` using `logging.conf`. 
    - [calculator.py](https://github.com/dhanesh-kh/calculator-midterm/blob/master/calculator.py)
    - [logging.conf](https://github.com/dhanesh-kh/calculator-midterm/blob/master/logging.conf)
- Sample log output:
    ```
    2024-07-01 09:37:02,584 - calculator - INFO - Starting Calculator Application
    2024-07-01 09:37:02,584 - calculator - INFO - Calculator mode: standard
    2024-07-01 09:37:02,586 - calculator.history - DEBUG - Loaded history from file: .\calculator\history\history.csv
    2024-07-01 09:37:02,586 - calculator - INFO - CalculatorController started.
    2024-07-01 09:37:05,442 - calculator - DEBUG - User input: 10+10
    2024-07-01 09:37:05,442 - calculator - DEBUG - Evaluating expression: 10+10
    2024-07-01 09:37:05,443 - calculator - DEBUG - Adding: 10.0 + 10.0
    2024-07-01 09:37:05,445 - calculator.history - DEBUG - Added entry to history: 10+10 = 20.0
    2024-07-01 09:37:05,447 - calculator - DEBUG - Displayed result: 20.0
    2024-07-01 09:37:05,447 - calculator - INFO - Evaluated expression: 10+10 = 20.0
    2024-07-01 09:37:38,267 - calculator - DEBUG - User input: a+b
    2024-07-01 09:37:38,268 - calculator - DEBUG - Evaluating expression: a+b
    2024-07-01 09:37:38,268 - calculator - ERROR - Invalid expression format: a+b
    2024-07-01 09:37:38,268 - calculator - ERROR - Displayed error: Error: Invalid expression format. Use: <operand1> <operator> <operand2>
    2024-07-01 09:37:38,268 - calculator - ERROR - Error evaluating expression: Invalid expression format. Use: <operand1> <operator> <operand2>
    2024-07-01 09:42:08,530 - calculator - DEBUG - User input: exit
    2024-07-01 09:42:08,532 - calculator - INFO - Displayed message: Exiting the calculator.
    2024-07-01 09:42:08,532 - calculator - INFO - User exited the application.
    ```

### Error Handling
The project employs both "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) error handling strategies.

* LBYL: Used in `CalculatorHistory` to check for existing entries before adding new ones.
    - `add_entry` function in [calculator_history.py](https://github.com/dhanesh-kh/calculator-midterm/blob/master/history/calculator_history.py)
* EAFP: Applied in exception handling blocks throughout the application to handle unexpected errors.
    - `run` function in [controller.py](https://github.com/dhanesh-kh/calculator-midterm/blob/master/controller.py)
    - `load_history` function in [calculator_history.py](https://github.com/dhanesh-kh/calculator-midterm/blob/master/history/calculator_history.py)