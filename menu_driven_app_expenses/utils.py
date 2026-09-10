from exceptions import InvalidExpenseError


def validate_description(description):
    if not description or not description.strip():
        raise InvalidExpenseError("Expense description cannot be empty.")
    return description.strip()


def validate_amount(amount_str):
    try:
        amount = float(amount_str)
    except (ValueError, TypeError):
        raise InvalidExpenseError(f"Invalid amount: '{amount_str}'. Must be a number.")
    if amount <= 0:
        raise InvalidExpenseError(f"Amount must be positive. Got: {amount}")
    return amount


def validate_category(category):
    valid = ["Food", "Transport", "Entertainment", "Bills", "General"]
    cat = category.strip().title() if category else "General"
    if cat not in valid:
        cat = "General"
    return cat
