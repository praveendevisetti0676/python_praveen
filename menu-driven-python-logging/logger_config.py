import logging
from pathlib import Path


LOG_DIRECTORY = Path("logs")

APPLICATION_LOG = LOG_DIRECTORY / "application.log"
ERROR_LOG = LOG_DIRECTORY / "error.log"


def setup_logging():
    """Configure application and error log files."""

    LOG_DIRECTORY.mkdir(exist_ok=True)

    logger = logging.getLogger("menu_app")

    logger.setLevel(logging.DEBUG)

    # Avoid adding handlers multiple times
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # Application log - DEBUG and above
    application_handler = logging.FileHandler(
        APPLICATION_LOG,
        encoding="utf-8"
    )

    application_handler.setLevel(logging.DEBUG)
    application_handler.setFormatter(formatter)

    # Error log - WARNING and above
    error_handler = logging.FileHandler(
        ERROR_LOG,
        encoding="utf-8"
    )

    error_handler.setLevel(logging.WARNING)
    error_handler.setFormatter(formatter)

    logger.addHandler(application_handler)
    logger.addHandler(error_handler)

    return logger

#| Level    | Meaning                        | Example               |
#| -------- | ------------------------------ | --------------------- |
#| DEBUG    | Detailed developer information | Login attempt         |
#| INFO     | Normal successful event        | User logged in        |
#| WARNING  | Something unexpected           | File is empty         |
#| ERROR    | Operation failed               | File cannot be opened |
#| CRITICAL | Serious application failure    | Unexpected failure    |
