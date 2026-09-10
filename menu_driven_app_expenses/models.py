from datetime import datetime


class Expense:
    def __init__(self, description, amount, category="General", date=None, expense_id=None):
        self.expense_id = expense_id or id(self)
        self.description = description
        self.amount = float(amount)
        self.category = category
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "expense_id": self.expense_id,
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            description=data["description"],
            amount=data["amount"],
            category=data.get("category", "General"),
            date=data.get("date"),
            expense_id=data.get("expense_id"),
        )

    def __str__(self):
        return (
            f"[{self.expense_id}] {self.date} | {self.category:12s} | "
            f"${self.amount:>8.2f} | {self.description}"
        )
