import logging


logging.basicConfig(
    filename="result_calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_logger():
    """Return the configured application logger."""
    return logging.getLogger(__name__)