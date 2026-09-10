import logging
from expense_tracker.expense_manager import ExpenseManager
from expense_tracker.storage import Storage
from utils import validate_description, validate_amount, validate_category
from exceptions import InvalidExpenseError, ExpenseNotFoundError, StorageError

logger = logging.getLogger(__name__)

_manager = None


def get_manager(storage_file):
    global _manager
    if _manager is None:
        storage = Storage(storage_file)
        _manager = ExpenseManager(storage)
        _manager.load()
    return _manager


def add_new_expense(storage_file, description, amount_str, category="General"):
    try:
        desc = validate_description(description)
        amt = validate_amount(amount_str)
        cat = validate_category(category)
        manager = get_manager(storage_file)
        expense = manager.add_expense(desc, amt, cat)
        return expense
    except InvalidExpenseError:
        raise
    except StorageError:
        raise
    except Exception as exc:
        logger.error(f"Unexpected error adding expense: {exc}")
        raise


def list_all_expenses(storage_file):
    manager = get_manager(storage_file)
    return manager.list_expenses()


def search_expenses(storage_file, keyword):
    manager = get_manager(storage_file)
    return manager.search_expenses(filter_keyword(keyword))


def filter_by_category(storage_file, category):
    manager = get_manager(storage_file)
    return manager.filter_by_category(category.strip())


def calculate_total(storage_file):
    manager = get_manager(storage_file)
    return manager.total()


def delete_expense_by_id(storage_file, expense_id):
    manager = get_manager(storage_file)
    return manager.delete_expense(expense_id)


def get_expense_by_id(storage_file, expense_id):
    manager = get_manager(storage_file)
    return manager.get_expense(expense_id)


def filter_keyword(keyword):
    if not keyword or not keyword.strip():
        raise InvalidExpenseError("Search keyword cannot be empty.")
    return keyword.strip()
