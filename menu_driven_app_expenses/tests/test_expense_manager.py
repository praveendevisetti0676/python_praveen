import os
import sys
import json
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from models import Expense
from utils import validate_description, validate_amount, validate_category
from exceptions import InvalidExpenseError, ExpenseNotFoundError
from expense_tracker.storage import Storage
from expense_tracker.expense_manager import ExpenseManager


class TestExpenseModel(unittest.TestCase):
    def test_create_expense(self):
        e = Expense("Lunch", 12.50, "Food")
        self.assertEqual(e.description, "Lunch")
        self.assertEqual(e.amount, 12.50)
        self.assertEqual(e.category, "Food")
        self.assertIsNotNone(e.expense_id)
        self.assertIsNotNone(e.date)

    def test_to_dict_and_from_dict(self):
        e = Expense("Bus fare", 3.00, "Transport")
        d = e.to_dict()
        e2 = Expense.from_dict(d)
        self.assertEqual(e2.description, "Bus fare")
        self.assertEqual(e2.amount, 3.00)
        self.assertEqual(e2.category, "Transport")

    def test_str_representation(self):
        e = Expense("Coffee", 4.50, "Food")
        s = str(e)
        self.assertIn("Coffee", s)
        self.assertIn("4.50", s)
        self.assertIn("Food", s)


class TestValidation(unittest.TestCase):
    def test_validate_description_valid(self):
        self.assertEqual(validate_description("Groceries"), "Groceries")

    def test_validate_description_empty(self):
        with self.assertRaises(InvalidExpenseError):
            validate_description("")

    def test_validate_description_whitespace(self):
        with self.assertRaises(InvalidExpenseError):
            validate_description("   ")

    def test_validate_amount_valid(self):
        self.assertEqual(validate_amount("25.50"), 25.50)

    def test_validate_amount_invalid(self):
        with self.assertRaises(InvalidExpenseError):
            validate_amount("abc")

    def test_validate_amount_negative(self):
        with self.assertRaises(InvalidExpenseError):
            validate_amount("-10")

    def test_validate_amount_zero(self):
        with self.assertRaises(InvalidExpenseError):
            validate_amount("0")

    def test_validate_category_valid(self):
        self.assertEqual(validate_category("Food"), "Food")

    def test_validate_category_unknown_defaults(self):
        self.assertEqual(validate_category("SomethingRandom"), "General")

    def test_validate_category_empty_defaults(self):
        self.assertEqual(validate_category(""), "General")


class TestStorage(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
        self.tmp.close()
        self.storage = Storage(self.tmp.name)

    def tearDown(self):
        if os.path.exists(self.tmp.name):
            os.remove(self.tmp.name)

    def test_load_empty_file(self):
        with open(self.tmp.name, "w") as f:
            json.dump([], f)
        self.assertEqual(self.storage.load_expenses(), [])

    def test_load_nonexistent_file(self):
        s = Storage("nonexistent_file.json")
        self.assertEqual(s.load_expenses(), [])

    def test_save_and_load(self):
        data = [{"expense_id": 1, "description": "Test", "amount": 5.0, "category": "Food", "date": "2025-01-01"}]
        self.storage.save_expenses(data)
        loaded = self.storage.load_expenses()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["description"], "Test")


class TestExpenseManager(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
        self.tmp.close()
        self.storage = Storage(self.tmp.name)
        self.manager = ExpenseManager(self.storage)

    def tearDown(self):
        if os.path.exists(self.tmp.name):
            os.remove(self.tmp.name)

    def test_add_and_list(self):
        self.manager.add_expense("Lunch", 12.00, "Food")
        expenses = self.manager.list_expenses()
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0].description, "Lunch")

    def test_total(self):
        self.manager.add_expense("A", 10.0)
        self.manager.add_expense("B", 20.0)
        self.assertEqual(self.manager.total(), 30.0)

    def test_search(self):
        self.manager.add_expense("Coffee", 4.0)
        self.manager.add_expense("Bus", 3.0)
        results = self.manager.search_expenses("coffee")
        self.assertEqual(len(results), 1)

    def test_filter_category(self):
        self.manager.add_expense("Lunch", 10.0, "Food")
        self.manager.add_expense("Movie", 15.0, "Entertainment")
        results = self.manager.filter_by_category("Food")
        self.assertEqual(len(results), 1)

    def test_delete_expense(self):
        exp = self.manager.add_expense("Delete me", 5.0)
        self.manager.delete_expense(exp.expense_id)
        self.assertEqual(len(self.manager.list_expenses()), 0)

    def test_delete_nonexistent_raises(self):
        with self.assertRaises(ExpenseNotFoundError):
            self.manager.delete_expense(99999)

    def test_get_nonexistent_raises(self):
        with self.assertRaises(ExpenseNotFoundError):
            self.manager.get_expense(99999)

    def test_persistence(self):
        self.manager.add_expense("Persist", 7.0, "Bills")
        manager2 = ExpenseManager(self.storage)
        manager2.load()
        self.assertEqual(len(manager2.list_expenses()), 1)


if __name__ == "__main__":
    unittest.main()
