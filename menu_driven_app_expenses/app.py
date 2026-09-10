import os
import logging
import config
from exceptions import InvalidExpenseError, ExpenseNotFoundError, StorageError
import services

os.makedirs(config.LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(config.LOG_FILE),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


def display_menu():
    print("\n===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expenses")
    print("4. Filter by Category")
    print("5. Calculate Total")
    print("6. Delete Expense")
    print("7. Exit")
    print("====================================")


def handle_add():
    desc = input("Enter description: ").strip()
    amt = input("Enter amount: ").strip()
    cat = input("Enter category (Food/Transport/Entertainment/Bills/General) [General]: ").strip()
    try:
        expense = services.add_new_expense(config.DATA_FILE, desc, amt, cat or "General")
        print(f"\nExpense added successfully!\n{expense}")
    except InvalidExpenseError as exc:
        print(f"\nError: {exc}")
    except StorageError as exc:
        print(f"\nStorage Error: {exc}")
    except Exception as exc:
        logger.error(f"Unexpected error: {exc}")
        print("\nAn unexpected error occurred. Please try again.")


def handle_list():
    expenses = services.list_all_expenses(config.DATA_FILE)
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    print("\n--- All Expenses ---")
    for e in expenses:
        print(e)
    print(f"\nTotal: ${services.calculate_total(config.DATA_FILE):.2f}")


def handle_search():
    keyword = input("Enter search keyword: ").strip()
    try:
        results = services.search_expenses(config.DATA_FILE, keyword)
        if not results:
            print(f"\nNo expenses matching '{keyword}'.")
            return
        print(f"\n--- Search Results for '{keyword}' ---")
        for e in results:
            print(e)
    except InvalidExpenseError as exc:
        print(f"\nError: {exc}")


def handle_filter():
    cat = input("Enter category (Food/Transport/Entertainment/Bills/General): ").strip()
    results = services.filter_by_category(config.DATA_FILE, cat)
    if not results:
        print(f"\nNo expenses in category '{cat}'.")
        return
    print(f"\n--- Expenses in '{cat}' ---")
    for e in results:
        print(e)


def handle_total():
    total = services.calculate_total(config.DATA_FILE)
    print(f"\nTotal Expenses: ${total:.2f}")


def handle_delete():
    expenses = services.list_all_expenses(config.DATA_FILE)
    if not expenses:
        print("\nNo expenses to delete.")
        return
    print("\n--- All Expenses ---")
    for e in expenses:
        print(e)
    try:
        eid = int(input("\nEnter expense ID to delete: ").strip())
        removed = services.delete_expense_by_id(config.DATA_FILE, eid)
        print(f"\nDeleted: {removed}")
    except (ValueError, TypeError):
        print("\nInvalid ID. Please enter a number.")
    except ExpenseNotFoundError as exc:
        print(f"\nError: {exc}")
    except StorageError as exc:
        print(f"\nStorage Error: {exc}")


def main():
    logger.info("Application started")
    print("Welcome to Personal Expense Tracker!")

    while True:
        display_menu()
        choice = input("Select an option (1-7): ").strip()

        try:
            if choice == "1":
                handle_add()
            elif choice == "2":
                handle_list()
            elif choice == "3":
                handle_search()
            elif choice == "4":
                handle_filter()
            elif choice == "5":
                handle_total()
            elif choice == "6":
                handle_delete()
            elif choice == "7":
                logger.info("Application shutting down")
                print("\nGoodbye!")
                break
            else:
                print("\nInvalid option. Please select 1-7.")
        except KeyboardInterrupt:
            logger.info("Application interrupted by user")
            print("\n\nGoodbye!")
            break
        except Exception as exc:
            logger.error(f"Unhandled exception: {exc}")
            print("\nAn unexpected error occurred. The application will continue.")


if __name__ == "__main__":
    main()
