from .exceptions import InvalidOperationError

def _validate_numbers(a, b):
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("First value must be a number.")

    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("Second value must be a number.")


def add(a, b):
    _validate_numbers(a, b)
    return a + b


def subtract(a, b):
    _validate_numbers(a, b)
    return a - b


def multiply(a, b):
    _validate_numbers(a, b)
    return a * b


def divide(a, b):
    _validate_numbers(a, b)

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


def percentage(value, percent):
    _validate_numbers(value, percent)

    if percent < 0:
        raise ValueError("Percentage cannot be negative.")

    return value * percent / 100


def calculate(operation, a, b):
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

    if operation not in operations:
        raise InvalidOperationError(
            f"Unsupported operation: {operation}"
        )

    return operations[operation](a, b)