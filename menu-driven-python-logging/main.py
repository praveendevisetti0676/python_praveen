from authentication import login, logout
from calculator import calculate
from file_operations import read_file, write_file
from exceptions import (
    AuthenticationError,
    CalculationError,
    FileOperationError
)
from logger_config import setup_logging


logger = setup_logging()


def show_menu():
    """Display the main application menu."""

    print("\n" + "=" * 45)
    print("        MENU DRIVEN PYTHON APPLICATION")
    print("=" * 45)
    print("1. Login")
    print("2. Calculate")
    print("3. Read a File")
    print("4. Write a File")
    print("5. Logout")
    print("6. Exit")
    print("=" * 45)


def perform_calculation():
    """Read calculation input and display result."""

    try:

        number1 = float(
            input("Enter first number: ")
        )

        number2 = float(
            input("Enter second number: ")
        )

        operation = input(
            "Enter operation (+, -, *, /): "
        ).strip()

        result = calculate(
            number1,
            number2,
            operation,
            logger
        )

        print(
            f"Result: {result}"
        )

    except ValueError as error:

        logger.error(
            f"Invalid numeric input: {error}"
        )

        print(
            "Error: Please enter valid numbers."
        )

    except CalculationError as error:

        logger.error(
            f"Calculation error: {error}"
        )

        print(
            f"Error: {error}"
        )


def perform_read():
    """Read a file."""

    filename = input(
        "Enter filename to read: "
    ).strip()

    try:

        read_file(
            filename,
            logger
        )

    except FileOperationError as error:

        print(
            f"Error: {error}"
        )


def perform_write():
    """Write content to a file."""

    filename = input(
        "Enter filename to write: "
    ).strip()

    content = input(
        "Enter content: "
    )

    try:

        write_file(
            filename,
            content,
            logger
        )

    except FileOperationError as error:

        print(
            f"Error: {error}"
        )


def main():
    """Run the menu-driven application."""

    logger.debug(
        "Application started"
    )

    logged_in = False
    username = None

    while True:

        show_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        try:

            if choice == "1":

                username = input(
                    "Username: "
                ).strip()

                password = input(
                    "Password: "
                ).strip()

                login(
                    username,
                    password,
                    logger
                )

                logged_in = True

                print(
                    "Login successful."
                )

            elif choice == "2":

                if not logged_in:

                    logger.warning(
                        "Calculation attempted without login"
                    )

                    print(
                        "Please login first."
                    )

                    continue

                perform_calculation()

            elif choice == "3":

                if not logged_in:

                    logger.warning(
                        "File read attempted without login"
                    )

                    print(
                        "Please login first."
                    )

                    continue

                perform_read()

            elif choice == "4":

                if not logged_in:

                    logger.warning(
                        "File write attempted without login"
                    )

                    print(
                        "Please login first."
                    )

                    continue

                perform_write()

            elif choice == "5":

                if logged_in:

                    logout(
                        username,
                        logger
                    )

                    logged_in = False
                    username = None

                else:

                    logger.warning(
                        "Logout attempted without login"
                    )

                    print(
                        "No user is currently logged in."
                    )

            elif choice == "6":

                logger.info(
                    "Application exited normally"
                )

                print(
                    "Thank you for using the application."
                )

                break

            else:

                logger.warning(
                    f"Invalid menu choice: {choice}"
                )

                print(
                    "Invalid choice. Please select 1-6."
                )

        except AuthenticationError as error:

            logger.error(
                f"Authentication error: {error}"
            )

            print(
                f"Login Error: {error}"
            )

        except Exception as error:

            logger.critical(
                f"Unexpected application failure: {error}",
                exc_info=True
            )

            print(
                "Critical Error: "
                "Unexpected application failure."
            )

            print(
                "The application will continue."
            )


if __name__ == "__main__":
    main()