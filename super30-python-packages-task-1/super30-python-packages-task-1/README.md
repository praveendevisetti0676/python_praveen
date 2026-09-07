# Python Packages Task 1 – Calculator Tools

## 📌 Objective

Build a reusable Python package instead of writing all functionality inside a single Python file.

This task demonstrates the difference between:

* **Function**
* **Module**
* **Package**
* **Import**
* **Custom Exception**
* **Error Handling**
* **Reusable Code**

The package provides functionality for:

* Basic arithmetic operations
* Percentage calculation
* Average calculation
* Temperature conversion
* Unit conversion
* Custom error handling
* Unsupported operation handling

---

# 📁 Project Structure

```text
super30-python-packages-task-1/
│
├── calculator_tools/
│   ├── __init__.py
│   ├── arithmetic.py
│   ├── statistics.py
│   ├── converter.py
│   └── exceptions.py
│
├── main.py
└── README.md
```

---

# 🧩 Files and Responsibilities

## 1. `calculator_tools/__init__.py`

This file makes `calculator_tools` a Python package and exposes the functions that can be imported easily.

Example:

```python
from calculator_tools import add
```

Instead of:

```python
from calculator_tools.arithmetic import add
```

---

## 2. `calculator_tools/arithmetic.py`

Contains basic arithmetic functionality.

Functions include:

```text
add()
subtract()
multiply()
divide()
percentage()
calculate()
```

The module also validates input values and handles:

* Invalid data types
* Division by zero
* Negative percentages
* Unsupported operations

---

## 3. `calculator_tools/statistics.py`

Contains statistical functionality.

Main function:

```python
calculate_average()
```

It calculates the average of numbers provided in a list or tuple.

Example:

```python
numbers = [10, 20, 30, 40, 50]

average = calculate_average(numbers)

print(average)
```

Output:

```text
30.0
```

It also handles:

* Invalid input types
* Empty lists
* Non-numeric values

---

## 4. `calculator_tools/converter.py`

Contains conversion functions.

### Temperature Conversion

```python
celsius_to_fahrenheit()
fahrenheit_to_celsius()
```

### Distance Conversion

```python
kilometers_to_miles()
miles_to_kilometers()
```

A general `convert()` function is also provided to demonstrate operation selection.

---

## 5. `calculator_tools/exceptions.py`

Contains the custom exception:

```python
class InvalidOperationError(Exception):
    pass
```

This exception is raised when an unsupported operation or conversion is requested.

Example:

```python
raise InvalidOperationError(
    "Unsupported operation"
)
```

---

# 🚀 How to Run the Project

Open PowerShell or Command Prompt and navigate to the project folder.

Run:

```powershell
python main.py
```

The program will demonstrate all the functionality provided by the package.

---

# ➕ Arithmetic Operations

The package supports:

```python
add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 5)
```

Expected results:

```text
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
```

---

# 📊 Percentage Calculation

The package provides:

```python
percentage(500, 10)
```

Output:

```text
50.0
```

This calculates:

```text
500 × 10 / 100 = 50
```

---

# 📈 Average Calculation

Example:

```python
numbers = [10, 20, 30, 40, 50]

calculate_average(numbers)
```

Output:

```text
30.0
```

---

# 🌡️ Temperature Conversion

### Celsius to Fahrenheit

```python
celsius_to_fahrenheit(25)
```

Output:

```text
77.0
```

### Fahrenheit to Celsius

```python
fahrenheit_to_celsius(77)
```

Output:

```text
25.0
```

---

# 📏 Unit Conversion

### Kilometers to Miles

```python
kilometers_to_miles(10)
```

Output:

```text
6.21371
```

### Miles to Kilometers

```python
miles_to_kilometers(10)
```

Output:

```text
16.0934
```

---

# ⚠️ Error Handling

The package demonstrates different types of error handling.

## 1. Division by Zero

```python
divide(10, 0)
```

Raises:

```text
ZeroDivisionError
```

Message:

```text
Cannot divide by zero.
```

---

## 2. Invalid Data Type

Example:

```python
add(10, "20")
```

Raises:

```text
TypeError
```

Message:

```text
First value must be a number.
```

---

## 3. Empty List

Example:

```python
calculate_average([])
```

Raises:

```text
ValueError
```

Message:

```text
Cannot calculate average of an empty list.
```

---

## 4. Unsupported Operation

Example:

```python
calculate("power", 10, 2)
```

Since `power` is not supported, the package raises:

```text
InvalidOperationError
```

This is our custom exception.

---

# 🛠️ Custom Exception

Python allows us to create our own exception classes.

In this project:

```python
class InvalidOperationError(Exception):
    pass
```

We use it when the user requests an operation that our package does not support.

For example:

```python
calculate("power", 10, 2)
```

The package recognizes that `"power"` is not a supported operation and raises:

```python
InvalidOperationError
```

This makes the error more meaningful and specific to our application.

---

# 🔄 Function → Module → Package → Import

One of the main goals of this task is understanding the relationship between functions, modules, packages, and imports.

## Function

A function performs a specific task.

Example:

```python
def add(a, b):
    return a + b
```

---

## Module

A Python file containing related functions, classes, and variables is called a module.

Example:

```text
arithmetic.py
```

contains:

```python
add()
subtract()
multiply()
divide()
```

---

## Package

A package is a directory containing related Python modules.

Example:

```text
calculator_tools/
```

contains:

```text
arithmetic.py
statistics.py
converter.py
exceptions.py
```

---

## Import

`import` allows us to use functionality from another module or package.

Example:

```python
from calculator_tools import add
```

---

# 📦 Package Architecture

```text
                    main.py
                       │
                       │ import
                       ▼
             ┌───────────────────┐
             │ calculator_tools  │
             │     PACKAGE       │
             └───────────────────┘
                 │      │      │
                 ▼      ▼      ▼
           arithmetic statistics converter
                 │      │      │
                 └──────┼──────┘
                        ▼
                  exceptions.py
```

The application is separated into smaller modules based on responsibility.

This makes the project:

* Easier to understand
* Easier to maintain
* Easier to test
* Easier to reuse
* Easier to extend

---

# 🔐 Input Validation

The package validates input before performing operations.

For example:

```python
if not isinstance(a, (int, float)) or isinstance(a, bool):
    raise TypeError("First value must be a number.")
```

This accepts:

```text
10
10.5
```

But rejects:

```text
"10"
True
False
```

The Boolean check is intentional because in Python:

```python
isinstance(True, int)
```

returns:

```text
True
```

Therefore, Boolean values are explicitly excluded from numeric input.

---

# 🔧 Internal Helper Functions

The project uses helper functions such as:

```python
_validate_numbers()
```

The leading underscore indicates that the function is intended for **internal use** within the module.

It is a naming convention, not a strict private mechanism.

For example:

```text
add()                 → Public function
divide()              → Public function
percentage()          → Public function

_validate_numbers()   → Internal/helper function
```

This avoids repeating the same validation logic in multiple functions.

---

# ▶️ `if __name__ == "__main__"`

The `main.py` file contains:

```python
if __name__ == "__main__":
    main()
```

This checks whether the file is being executed directly.

When we run:

```powershell
python main.py
```

Python sets:

```python
__name__ = "__main__"
```

Therefore:

```python
main()
```

is executed.

If another Python file imports `main.py`, the condition is false and `main()` does not automatically execute.

This makes the Python file reusable both as:

1. A directly executable program
2. An importable module

---

# 🧠 Key Concepts Learned

This task demonstrates the following Python concepts:

* Creating a Python package
* Creating Python modules
* Creating reusable functions
* Importing functions from packages
* Organizing code by responsibility
* Input validation
* `isinstance()`
* Built-in exceptions
* Custom exceptions
* `raise`
* `try` / `except`
* Helper functions
* Leading underscore naming convention
* Package `__init__.py`
* `if __name__ == "__main__"`
* Code reusability
* Modular programming

---

# 🎯 Learning Outcome

After completing this task, you should understand why we should avoid putting all functionality into one large Python file.

Instead, related functionality can be separated into modules:

```text
Arithmetic      → arithmetic.py
Statistics      → statistics.py
Conversions     → converter.py
Exceptions      → exceptions.py
Application     → main.py
```

These modules can then be grouped into a reusable package:

```text
calculator_tools
```

The overall concept is:

```text
Function
   ↓
Module
   ↓
Package
   ↓
Import
   ↓
Reusable Application
```

---

# 📌 Conclusion

This project demonstrates how Python packages help organize and reuse code.

Instead of creating one large program, we created a structured package containing multiple modules, reusable functions, input validation, error handling, and a custom exception.

The project provides a practical foundation for understanding **modular programming and Python package development**.
