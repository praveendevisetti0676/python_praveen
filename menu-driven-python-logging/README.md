# 🐍 Menu-Driven Python Application

A practical Python application demonstrating **modular programming, logging, exception handling, custom exceptions, file handling, and application recovery**.

The application provides a menu through which the user can:

1. Login
2. Calculate
3. Read a File
4. Write a File
5. Logout
6. Exit

The primary focus of this project is **Python Logging** and how different logging levels can be used to track application activity and errors.

---

## 🎯 Objective

The objective of this project is to create a menu-driven Python application that:

* Uses multiple Python modules
* Implements login and logout functionality
* Performs basic calculations
* Reads data from files
* Writes data to files
* Handles invalid user input
* Handles calculation errors
* Handles file-operation errors
* Uses custom exceptions
* Generates DEBUG, INFO, WARNING, ERROR and CRITICAL logs
* Stores logs in separate log files
* Continues running even when an operation fails

---

## 📁 Project Structure

```text
menu-driven-python-logging/
│
├── main.py
├── authentication.py
├── calculator.py
├── file_operations.py
├── logger_config.py
├── exceptions.py
├── data.txt
│
├── logs/
│   ├── application.log
│   └── error.log
│
└── README.md
```

---

## 🧩 Module Responsibilities

### `main.py`

The main application controller.

Responsibilities:

* Display the menu
* Accept user choices
* Maintain login state
* Call functions from other modules
* Handle exceptions
* Keep the application running

---

### `authentication.py`

Handles authentication-related operations.

Functions:

```python
login()
logout()
```

Responsibilities:

* Validate username and password
* Log login attempts
* Log successful login
* Log invalid login attempts
* Handle logout

Demo credentials:

```text
Username: admin
Password: admin123
```

---

### `calculator.py`

Handles mathematical operations.

Supported operations:

```text
+
-
*
/
```

Responsibilities:

* Perform calculations
* Validate operations
* Detect division by zero
* Generate calculation logs
* Raise `CalculationError` when required

---

### `file_operations.py`

Handles file-related operations.

Functions:

```python
read_file()
write_file()
```

Responsibilities:

* Read files
* Write files
* Detect missing files
* Detect empty files
* Handle permission errors
* Generate appropriate log messages

---

### `exceptions.py`

Contains application-specific custom exceptions.

```python
class AuthenticationError(Exception):
    """Raised when login credentials are invalid."""


class CalculationError(Exception):
    """Raised when a calculation cannot be completed."""


class FileOperationError(Exception):
    """Raised when a file operation fails."""
```

Custom exceptions make errors more meaningful and easier to handle.

---

### `logger_config.py`

Contains the complete logging configuration.

Responsibilities:

* Create the `logs` directory
* Configure the application logger
* Configure log levels
* Configure log formatting
* Create the application log handler
* Create the error log handler

---

## 📋 Application Menu

When the program starts, the following menu is displayed:

```text
=============================================
       MENU DRIVEN PYTHON APPLICATION
=============================================
1. Login
2. Calculate
3. Read a File
4. Write a File
5. Logout
6. Exit
=============================================
```

---

# 📝 Logging

Logging is the primary focus of this project.

Python provides five commonly used logging levels:

| Level      | Purpose                              | Example                  |
| ---------- | ------------------------------------ | ------------------------ |
| `DEBUG`    | Detailed diagnostic information      | Login attempt            |
| `INFO`     | Normal application activity          | User logged in           |
| `WARNING`  | Unexpected but recoverable situation | File was empty           |
| `ERROR`    | An operation failed                  | File could not be opened |
| `CRITICAL` | Serious unexpected failure           | Application failure      |

---

## 🔵 DEBUG

`DEBUG` is used for detailed information useful during development and troubleshooting.

Example:

```python
logger.debug("Application started")
```

Another example:

```python
logger.debug(
    f"Calculation requested: {number1} {operation} {number2}"
)
```

---

## 🟢 INFO

`INFO` represents normal successful application activity.

Example:

```python
logger.info("User logged in")
```

Another example:

```python
logger.info("Calculation completed")
```

---

## 🟡 WARNING

`WARNING` indicates something unexpected happened, but the application can continue.

Example:

```python
logger.warning("File was empty")
```

Another example:

```python
logger.warning("Invalid menu choice")
```

---

## 🔴 ERROR

`ERROR` indicates that an operation failed.

Example:

```python
logger.error("File could not be opened")
```

Another example:

```python
logger.error("Division by zero attempted")
```

---

## 🚨 CRITICAL

`CRITICAL` represents a serious unexpected application failure.

Example:

```python
logger.critical(
    "Unexpected application failure",
    exc_info=True
)
```

`exc_info=True` records exception information and traceback details in the log.

---

# 📂 Log Files

The application stores logs inside:

```text
logs/
```

Two log files are generated:

```text
logs/
├── application.log
└── error.log
```

---

## `application.log`

This file records all five logging levels:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

The application handler is configured at:

```python
logging.DEBUG
```

---

## `error.log`

This file records:

```text
WARNING
ERROR
CRITICAL
```

The error handler is configured at:

```python
logging.WARNING
```

Therefore, WARNING, ERROR and CRITICAL messages appear in both log files.

---

# 🔄 Logging Flow

The logging architecture can be represented as:

```text
                    Application
                         │
                         ▼
                       Logger
                         │
                DEBUG and above
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
     application.log             error.log
        DEBUG+                  WARNING+
```

More specifically:

```text
DEBUG     ───────────────► application.log

INFO      ───────────────► application.log

WARNING   ───────────────► application.log
                └────────► error.log

ERROR     ───────────────► application.log
                └────────► error.log

CRITICAL  ───────────────► application.log
                └────────► error.log
```

---

# ⚠️ Exception Handling

The application uses exception handling to prevent one failed operation from terminating the entire program.

General flow:

```text
User Operation
      │
      ▼
    try
      │
 ┌────┴────┐
 ▼         ▼
Success   Error
 │          │
 ▼          ▼
Continue  except
             │
             ▼
           Log Error
             │
             ▼
       Display Message
             │
             ▼
       Continue Program
```

---

## Example: Division by Zero

If the user enters:

```text
First number: 100
Second number: 0
Operation: /
```

The application detects the error:

```python
if number2 == 0:
    logger.error(
        "Division by zero attempted"
    )

    raise CalculationError(
        "Cannot divide by zero."
    )
```

The application displays:

```text
Error: Cannot divide by zero.
```

The application does **not** terminate.

The user can continue using the menu.

---

# 📄 File Handling

The project demonstrates both reading and writing files.

### Reading

```text
3. Read a File
```

The application checks:

* Whether the file exists
* Whether the file can be opened
* Whether the file is empty
* Whether the user has permission to read it

### Writing

```text
4. Write a File
```

The application writes user-provided content to the specified file.

---

# 🧪 Testing Scenarios

The following scenarios can be used to test the application.

## Test 1 — Successful Login

```text
Username: admin
Password: admin123
```

Expected:

```text
Login successful.
```

Log:

```text
INFO - User logged in: admin
```

---

## Test 2 — Invalid Login

```text
Username: admin
Password: wrong
```

Expected:

```text
Login Error: Invalid username or password.
```

Log:

```text
ERROR - Invalid login attempt
```

---

## Test 3 — Successful Calculation

Input:

```text
100
50
+
```

Expected:

```text
Result: 150.0
```

Logs:

```text
DEBUG - Calculation requested
INFO - Calculation completed
```

---

## Test 4 — Division by Zero

Input:

```text
100
0
/
```

Expected:

```text
Error: Cannot divide by zero.
```

Log:

```text
ERROR - Division by zero attempted
```

---

## Test 5 — Empty File

Read an empty file.

Expected:

```text
Warning: File is empty.
```

Log:

```text
WARNING - File was empty
```

---

## Test 6 — Missing File

Try to read a file that does not exist.

Expected:

```text
Error: File does not exist.
```

Log:

```text
ERROR - File could not be opened
```

---

## Test 7 — Invalid Menu Choice

Enter:

```text
99
```

Expected:

```text
Invalid choice. Please select 1-6.
```

Log:

```text
WARNING - Invalid menu choice
```

---

## Test 8 — Application Recovery

Perform an operation that generates an error.

For example:

```text
Calculate
100 / 0
```

The application displays an error but remains active.

The user can then select:

```text
Read a File
```

or:

```text
Write a File
```

This demonstrates that exception handling prevents one failure from terminating the application.

---

# ▶️ How to Run

Open a terminal in the project directory.

```powershell
cd menu-driven-python-logging
```

Run the application:

```powershell
python main.py
```

---

# 🔐 Demo Login

For demonstration purposes, the application uses:

```text
Username: admin
Password: admin123
```

> Note: This is only for educational purposes. A production application should never hard-code passwords.

---

# 🧠 Python Concepts Covered

This project demonstrates:

### Python Fundamentals

* Variables
* Functions
* Conditional statements
* Loops
* User input
* String formatting

### Modular Programming

* Creating modules
* Importing functions
* Separation of concerns
* Reusable functions

### Exception Handling

* `try`
* `except`
* `raise`
* Custom exceptions
* Exception propagation
* Recovery after errors

### File Handling

* `pathlib.Path`
* Reading files
* Writing files
* File existence checks
* File exceptions

### Logging

* `logging`
* Logger
* Handler
* Formatter
* Log levels
* File logging
* Multiple handlers
* `exc_info=True`

---

# 🏗️ Application Architecture

```text
                       main.py
                          │
          ┌───────────────┼────────────────┐
          │               │                │
          ▼               ▼                ▼
 authentication.py   calculator.py   file_operations.py
          │               │                │
          └───────────────┼────────────────┘
                          │
                          ▼
                   logger_config.py
                          │
                 ┌────────┴────────┐
                 ▼                 ▼
        application.log        error.log
```

Custom exceptions are defined separately:

```text
exceptions.py
      │
      ├── AuthenticationError
      ├── CalculationError
      └── FileOperationError
```

---

# 🌟 Key Learning

The main lesson from this project is:

> **Don't just make an application work — make it observable, recoverable and maintainable.**

A well-designed application should:

```text
Modular
   +
Validated
   +
Exception Safe
   +
Logged
   +
Maintainable
```

---

# 🚀 Possible Improvements

The project can be extended with:

* Multiple user accounts
* Password hashing
* Database-based authentication
* More mathematical operations
* CSV file support
* JSON file support
* Log rotation
* Console logging
* Configuration files
* Unit tests
* Automated testing
* User roles and permissions

---

# 📚 Learning Outcome

After completing this project, you should be able to:

1. Create a modular Python application.
2. Separate responsibilities across different modules.
3. Create custom exceptions.
4. Handle application errors using `try-except`.
5. Use Python's logging framework.
6. Understand DEBUG, INFO, WARNING, ERROR and CRITICAL.
7. Configure multiple logging handlers.
8. Store logs in separate files.
9. Handle file-operation errors.
10. Build applications that continue running after recoverable errors.

---

# 🎥 Video Tutorial

This project can also be used as a practical Python tutorial covering:

**Python Modules → Functions → Exception Handling → Custom Exceptions → File Handling → Logging → Error Recovery**

---

# 👨‍💻 Author

**Praveen Devisetti**

---

# 📜 License

This project is created for **educational and learning purposes**.

You are free to modify and extend the project for your own practice.
