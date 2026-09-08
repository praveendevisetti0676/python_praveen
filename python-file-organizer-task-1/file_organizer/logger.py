import logging


logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_success(message):
    logging.info(f"SUCCESS: {message}")


def log_error(message):
    logging.error(f"FAILED: {message}")