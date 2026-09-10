class InvalidExpenseError(Exception):
    """Raised when expense information is invalid."""


class ExpenseNotFoundError(Exception):
    """Raised when a requested expense cannot be found."""


class StorageError(Exception):
    """Raised when there is an error reading or writing data."""
