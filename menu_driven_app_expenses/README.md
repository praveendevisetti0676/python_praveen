# Personal Expense Tracker

A small command-line Python application built using **step-by-step vibe coding with an AI coding assistant**.

The application is designed to manage personal expenses from the command line while demonstrating Python modularity, packages, exception handling, custom exceptions, logging, imports between modules, testing, and refactoring.

---

## 1. Project Objective

The objective of this exercise is to build a small command-line application with the help of an AI coding assistant such as:

- Claude
- ChatGPT
- GitHub Copilot
- OpenCode
- Another AI coding assistant

The project is developed **step-by-step rather than asking AI to generate the complete project in one prompt**.

---

## 2. Application

### Personal Expense Tracker

The application allows a user to:

- Add a personal expense
- View recorded expenses
- Calculate total expenses
- Search/filter expenses
- Validate user input
- Handle application errors safely
- Record important application events in a log file

The application is intentionally kept small and command-line based so that the focus remains on **Python development practices and AI-assisted software development**.

---

## 3. Key Learning Requirements

This project demonstrates the following requirements from the exercise:

| Requirement | Implementation |
|---|---|
| At least 4 Python files/modules | Yes |
| At least one Python package | Yes |
| Imports between modules | Yes |
| `try/except/finally` | Yes |
| At least one custom exception | Yes |
| Logging to a file | Yes |
| Command-line application | Yes |
| README.md | Yes |
| AI-assisted step-by-step development | Yes |
| Refactoring | Yes |
| Testing | Yes |

---

## 4. Suggested Project Structure

```text
personal_expense_tracker/
│
├── app.py
├── config.py
├── models.py
├── services.py
├── exceptions.py
├── utils.py
│
├── expense_tracker/
│   ├── __init__.py
│   ├── expense_manager.py
│   └── storage.py
│
├── logs/
│   └── application.log
│
├── tests/
│   └── test_expense_manager.py
│
└── README.md
```

### Module Responsibilities

**`app.py`**
- Application entry point
- Displays the command-line menu
- Coordinates user interaction

**`config.py`**
- Stores configuration values
- Defines logging/file-related configuration

**`models.py`**
- Defines the expense data model

**`services.py`**
- Contains business logic such as adding, listing, searching, and calculating expenses

**`exceptions.py`**
- Contains custom application exceptions

**`utils.py`**
- Contains reusable helper and validation functions

**`expense_tracker/__init__.py`**
- Makes `expense_tracker` a Python package

**`expense_tracker/expense_manager.py`**
- Handles expense-management operations

**`expense_tracker/storage.py`**
- Handles reading/writing expense data

---

## 5. How the Application Works

The application follows a simple flow:

```text
User
  |
  v
Command-Line Menu
  |
  v
Input Validation
  |
  v
Expense Manager / Service Layer
  |
  +----> Storage
  |
  +----> Business Logic
  |
  v
Result displayed to User
  |
  v
Application Log
```

---

## 6. Exception Handling

The application uses Python exception handling to prevent unexpected application termination.

A typical flow is:

```python
try:
    # application operation
    pass
except SomeCustomException as exc:
    # handle expected application error
    pass
except Exception as exc:
    # handle unexpected error
    pass
finally:
    # cleanup / final action
    pass
```

The `finally` block ensures that required cleanup or final processing can take place even when an exception occurs.

---

## 7. Custom Exception

The project includes at least one application-specific exception.

Example:

```python
class InvalidExpenseError(Exception):
    """Raised when expense information is invalid."""
```

This allows the application to distinguish business/input validation errors from generic Python exceptions.

---

## 8. Logging

The application writes important events to a log file.

Example location:

```text
logs/application.log
```

Logging can capture events such as:

- Application startup
- Expense creation
- Validation failures
- File/storage errors
- Unexpected exceptions
- Application shutdown

Example:

```python
import logging

logging.info("Expense added successfully")
logging.error("Unable to save expense")
```

Logging makes it easier to troubleshoot the application without relying only on console output.

---

## 9. Running the Application

### Step 1: Open the project

Open the project folder in VS Code.

### Step 2: Open the terminal

In VS Code:

```text
Terminal → New Terminal
```

### Step 3: Run the application

For example:

```bash
python app.py
```

On some systems:

```bash
python3 app.py
```

### Step 4: Follow the command-line menu

Use the displayed options to add, view, search, or summarize expenses.

---

## 10. Testing

The final application should be tested for:

### Normal scenarios

- Add a valid expense
- View expenses
- Calculate the total
- Search for an expense
- Restart the application

### Error scenarios

- Empty expense description
- Invalid amount
- Negative amount
- Incorrect menu selection
- Missing/invalid data
- Storage/file errors
- Unexpected runtime errors

After testing, verify that the application:

1. Does not crash unexpectedly
2. Shows a meaningful error message
3. Logs important errors
4. Continues execution where appropriate

---

## 11. AI-Assisted Vibe Coding Process

The project was **not generated in one single AI prompt**.

The development process followed an iterative approach:

```text
Understand Requirement
        ↓
Design Structure
        ↓
Create One Module
        ↓
Run Application
        ↓
Observe Error
        ↓
Ask AI for Diagnosis/Fix
        ↓
Add Exception Handling
        ↓
Add Logging
        ↓
Refactor
        ↓
Test
        ↓
Final Review
```

This approach allows the developer to understand the code while using AI as a development assistant.

---

# 12. AI Prompts Used During Development

The following prompts document the step-by-step AI-assisted development process.

## Prompt 1 — Understand the Requirement

> I need to build a small command-line Python application for a coding exercise. Explain the requirements in simple terms and identify the minimum technical requirements I must satisfy. Do not generate the code yet.

### Purpose

Used to understand the assignment before writing code.

---

## Prompt 2 — Design the Module Structure

> For a Personal Expense Tracker command-line application, suggest a clean Python project structure with at least 4 modules and one package. Explain the responsibility of each file. Do not generate the complete application.

### Purpose

Used to design the project structure before implementation.

---

## Prompt 3 — Generate One Module

> Based on the proposed structure, generate only the `models.py` module for the Personal Expense Tracker. Keep the code simple and explain the classes/functions created. Do not generate any other files.

### Purpose

Used to implement the application one module at a time.

---

## Prompt 4 — Review an Error

> I ran the application and received the following error: [paste error here]. Explain the root cause, identify the affected module, and provide the smallest safe fix. Do not rewrite the entire project.

### Purpose

Used for iterative debugging after running the code.

---

## Prompt 5 — Add Exception Handling

> Review this module and add appropriate `try/except/finally` handling without changing its overall design. Also explain which errors should be handled explicitly and why.

### Purpose

Used to satisfy the exception-handling requirement while learning why the handling is needed.

---

## Prompt 6 — Add a Custom Exception

> Create a custom exception for invalid expense data and show how it should be raised and handled in the relevant module. Modify only the necessary code.

### Purpose

Used to introduce application-specific error handling.

---

## Prompt 7 — Add Logging

> Add Python logging to this application so important events and errors are written to `logs/application.log`. Show the changes needed in the relevant modules and explain the log levels used.

### Purpose

Used to add file-based logging.

---

## Prompt 8 — Refactor

> Review the current Personal Expense Tracker structure for duplicated logic, unclear responsibilities, and unnecessary complexity. Suggest improvements and then refactor only the affected modules.

### Purpose

Used to improve maintainability after the first working version.

---

## Prompt 9 — Test the Application

> Create test cases for the Personal Expense Tracker covering successful operations, invalid input, custom exceptions, and storage errors. Focus on practical tests rather than generating the entire project again.

### Purpose

Used to verify the completed implementation.

---

## Prompt 10 — Final Review

> Perform a final code review of this Personal Expense Tracker against the original assignment requirements. Check for 4+ Python modules, one package, imports between modules, try/except/finally, a custom exception, file logging, exception handling, and a README. Report anything missing without rewriting the complete project.

### Purpose

Used for final compliance verification.

---

## 13. Important Vibe Coding Principle

The main objective of this exercise is not simply to produce working code.

The goal is to demonstrate that AI was used as an **iterative coding assistant**.

The developer should understand and participate in each stage:

- Requirement understanding
- Architecture/design
- Module creation
- Execution
- Debugging
- Exception handling
- Logging
- Refactoring
- Testing
- Final review

This makes the development process more transparent and demonstrates practical AI-assisted software engineering.

---

## 14. Example Git/Development Workflow

A simple development sequence can be maintained using commits such as:

```text
1. Initial project structure
2. Add expense model
3. Add expense manager
4. Add storage module
5. Add command-line interface
6. Add custom exception
7. Add exception handling
8. Add logging
9. Refactor modules
10. Add tests
11. Final documentation
```

This makes the step-by-step development journey easier to demonstrate.

---

## 15. Final Checklist

Before submitting the project, verify:

```text
[ ] Application runs from the command line
[ ] At least 4 Python modules exist
[ ] At least 1 Python package exists
[ ] __init__.py is present
[ ] Modules import each other appropriately
[ ] try/except/finally is implemented
[ ] Custom exception is implemented
[ ] Logging writes to a file
[ ] Errors are handled gracefully
[ ] Application has been tested
[ ] Code has been refactored
[ ] README.md is included
[ ] At least 5 AI prompts are documented
```

---

## 16. Conclusion

This project demonstrates a practical approach to **AI-assisted Python development using step-by-step vibe coding**.

Instead of asking an AI assistant to generate the entire solution in one prompt, the project is developed incrementally by:

1. Understanding the requirements
2. Designing the project structure
3. Building individual modules
4. Running and debugging the application
5. Adding exception handling
6. Adding custom exceptions
7. Adding file-based logging
8. Refactoring the implementation
9. Testing the final application
10. Documenting the AI prompts and development process
