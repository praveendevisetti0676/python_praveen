class InvalidMarksError(Exception):
    """Raised when marks are outside the range 0 to 100."""


class MissingStudentInfoError(Exception):
    """Raised when required student information is missing."""