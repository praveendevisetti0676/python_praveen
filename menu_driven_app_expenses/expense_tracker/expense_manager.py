import logging
from expense_tracker.storage import Storage
from models import Expense
from exceptions import ExpenseNotFoundError, InvalidExpenseError

logger = logging.getLogger(__name__)


class ExpenseManager:
    def __init__(self, storage):
        self.storage = storage
        self._expenses = []

    def load(self):
        data = self.storage.load_expenses()
        self._expenses = [Expense.from_dict(d) for d in data]

    def add_expense(self, description, amount, category="General"):
        expense = Expense(description=description, amount=amount, category=category)
        self._expenses.append(expense)
        self._save()
        logger.info(f"Expense added: {expense}")
        return expense

    def list_expenses(self):
        return list(self._expenses)

    def get_expense(self, expense_id):
        for e in self._expenses:
            if e.expense_id == expense_id:
                return e
        raise ExpenseNotFoundError(f"Expense with id {expense_id} not found.")

    def delete_expense(self, expense_id):
        for i, e in enumerate(self._expenses):
            if e.expense_id == expense_id:
                removed = self._expenses.pop(i)
                self._save()
                logger.info(f"Expense deleted: {removed}")
                return removed
        raise ExpenseNotFoundError(f"Expense with id {expense_id} not found.")

    def search_expenses(self, keyword):
        keyword_lower = keyword.lower()
        return [e for e in self._expenses if keyword_lower in e.description.lower() or keyword_lower in e.category.lower()]

    def filter_by_category(self, category):
        cat_lower = category.lower()
        return [e for e in self._expenses if e.category.lower() == cat_lower]

    def total(self):
        return sum(e.amount for e in self._expenses)

    def _save(self):
        data = [e.to_dict() for e in self._expenses]
        self.storage.save_expenses(data)
