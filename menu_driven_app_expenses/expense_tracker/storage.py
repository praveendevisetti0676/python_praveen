import json
import logging
import os
from exceptions import StorageError

logger = logging.getLogger(__name__)


class Storage:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_expenses(self):
        if not os.path.exists(self.filepath):
            logger.info("No data file found. Starting with empty list.")
            return []
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
            logger.info(f"Loaded {len(data)} expenses from {self.filepath}")
            return data
        except (json.JSONDecodeError, IOError) as exc:
            logger.error(f"Failed to load expenses: {exc}")
            raise StorageError(f"Could not read expense data: {exc}") from exc

    def save_expenses(self, expenses):
        try:
            with open(self.filepath, "w") as f:
                json.dump(expenses, f, indent=2)
            logger.info(f"Saved {len(expenses)} expenses to {self.filepath}")
        except IOError as exc:
            logger.error(f"Failed to save expenses: {exc}")
            raise StorageError(f"Could not save expense data: {exc}") from exc
