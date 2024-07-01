class CalculatorView:
    def get_input(self) -> str:
        return input("Enter expression (or type 'exit' to quit): ")

    def display_result(self, result: float):
        print(f"Result: {result}")

    def display_error(self, message: str):
        print(message)

    def display_message(self, message: str):
        print(message)
