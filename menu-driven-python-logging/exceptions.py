class AuthenticationError(Exception):
    """Raised when login credentials are invalid."""


class CalculationError(Exception):
    """Raised when a calculation cannot be completed."""


class FileOperationError(Exception):
    """Raised when a file operation fails."""