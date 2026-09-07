
# 🐍 Python Functions — Task 1

## 📌 Project Overview

This repository contains **Python Functions — Task 1**, designed to build a strong understanding of **user-defined functions** and the fundamentals of reusable programming.

The task focuses on creating functions with:

* Parameters
* Arguments
* Return values
* Default arguments
* Positional arguments
* Keyword arguments
* Function documentation using docstrings
* Reusable problem-solving logic

All problem-solving logic is implemented **inside the functions**, as required by the assignment.

---

## 🎯 Objective

The objective of this task is to learn how to:

1. Define custom functions using `def`
2. Pass parameters to functions
3. Call functions using arguments
4. Return values from functions
5. Use default arguments
6. Use positional arguments
7. Use keyword arguments
8. Write reusable and modular code
9. Add docstrings to custom functions
10. Understand the difference between `print()` and `return`

---

# 📚 Programs Included

The task contains **12 Jupyter Notebook programs**.

| #  | Notebook                                                                                                                                                            | Topic                          | Main Function(s)                                |
| -- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ----------------------------------------------- |
| 01 | [`01_add_two_numbers.ipynb`](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-functions-task-1/01_add_two_numbers.ipynb)             | Addition & Function Basics     | `add()`                                         |
| 02 | [`02_arithmetic_operations.ipynb`](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-functions-task-1/02_arithmetic_operations.ipynb) | Arithmetic Operations          | `add()`, `subtract()`, `multiply()`, `divide()` |
| 03 | [`03_even_or_odd.ipynb`](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-functions-task-1/03_even_or_odd.ipynb)                     | Even or Odd                    | `check_even_odd()`                              |
| 04 | [`04_largest_of_three.ipynb`](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python_functions-task-1/04_largest_of_three.ipynb)           | Largest of Three Numbers       | `largest_of_three()`                            |
| 05 | [`05_factorial_function.ipynb`](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-functions-task-1/05_factorial_function.ipynb)       | Factorial                      | `factorial()`                                   |
| 06 | [`06_prime_checker.ipynb`](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-functions-task-1/06_prime_checker.ipynb)                 | Prime Number Check             | `is_prime()`                                    |
| 07 | [`07_calculate_discount.ipynb`](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-functions-task-1/07_calculate_discount.ipynb)       | Default Arguments              | `calculate_discount()`                          |
| 08 | [`08_list_sum_function.ipynb`](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-functions-task-1/08_list_sum_function.ipynb)         | List Sum                       | `calculate_list_sum()`                          |
| 09 | [`09_count_vowels.ipynb`](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-functions-task-1/09_count_vowels.ipynb)                   | String Processing              | `count_vowels()`                                |
| 10 | [`10_palindrome_function.ipynb`](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-functions-task-1/10_palindrome_function.ipynb)     | Palindrome                     | `is_palindrome()`                               |
| 11 | [`11_student_profile.ipynb`](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-functions-task-1/11_student_profile.ipynb)             | Positional & Keyword Arguments | `student_profile()`                             |
| 12 | [`12_print_vs_return.ipynb`](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-functions-task-1/12_print_vs_return.ipynb)             | `print()` vs `return`          | `add_using_print()`, `add_using_return()`       |

> **Note:** The notebook links above point to the corresponding files in the GitHub repository.

---

# 🧩 Program Details

## 01. Add Two Numbers

### Function

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

### Concepts

* Function definition
* Parameters
* Arguments
* Return value
* Function call

---

## 02. Arithmetic Operations

This program demonstrates the four basic arithmetic operations using functions.

### Functions

```python
add()
subtract()
multiply()
divide()
```

### Operations

* Addition
* Subtraction
* Multiplication
* Division

The division function also handles division by zero.

---

## 03. Even or Odd

Checks whether a given number is even or odd.

### Function

```python
def check_even_odd(number):
    """Return whether a number is even or odd."""
    
    if number % 2 == 0:
        return "Even"
    
    return "Odd"
```

### Concept

The program uses the **modulus operator `%`** to determine whether the number is divisible by 2.

---

## 04. Largest of Three Numbers

Finds the largest of three numbers **without using `max()`**.

### Function

```python
def largest_of_three(a, b, c):
    """Return the largest of three numbers without using max()."""
```

### Concepts

* Parameters
* Conditional statements
* Function return value
* Reusable logic

---

## 05. Factorial Function

Calculates the factorial of a number using a function.

### Function

```python
def factorial(number):
    """Return the factorial of a non-negative integer."""
```

### Example

```text
5! = 5 × 4 × 3 × 2 × 1 = 120
```

### Concepts

* Functions
* Parameters
* `for` loop
* Accumulation
* Return value

---

## 06. Prime Checker

Checks whether a number is a prime number.

### Function

```python
def is_prime(number):
    """Return True if a number is prime, otherwise return False."""
```

### Example

```text
17 → Prime
10 → Not Prime
```

### Concepts

* Functions
* Parameters
* Loops
* Conditional statements
* Boolean return values

---

## 07. Calculate Discount

Demonstrates the use of a **default argument**.

### Function

```python
def calculate_discount(price, discount=10):
    """Return the final price after applying the discount percentage."""
```

The default discount is:

```python
discount=10
```

Therefore:

```python
calculate_discount(1000)
```

automatically applies a **10% discount**.

A different discount can also be supplied:

```python
calculate_discount(1000, 20)
```

### Concept Demonstrated

**Default argument**

---

## 08. List Sum Function

Calculates the sum of list elements **without using the built-in `sum()` function**.

### Function

```python
def calculate_list_sum(numbers):
    """Return the sum of list elements without using sum()."""
```

### Example

```python
numbers = [10, 20, 30, 40]

result = calculate_list_sum(numbers)

print(result)
```

Output:

```text
100
```

### Concepts

* Lists
* Loops
* Functions
* Accumulator pattern
* Return values

---

## 09. Count Vowels

Counts the number of vowels in a string.

### Function

```python
def count_vowels(text):
    """Return the number of vowels in a string."""
```

### Example

```python
count_vowels("Python Programming")
```

### Concepts

* Strings
* Loops
* String methods
* Functions
* Return values

---

## 10. Palindrome Function

Checks whether a string is a palindrome.

### Function

```python
def is_palindrome(text):
    """Return True if the text is a palindrome, otherwise return False."""
```

### Example

```python
is_palindrome("madam")
```

Output:

```text
True
```

### Concepts

* Strings
* String slicing
* Functions
* Boolean return values

---

# 11. Student Profile

This program demonstrates **positional arguments and keyword arguments**.

### Function

```python
def student_profile(name, age, course):
    """Return a formatted student profile."""
    
    profile = f"Name : {name}\nAge : {age}\nCourse : {course}"
    
    return profile
```

### Positional Arguments

```python
profile1 = student_profile("Rahul", 30, "Python")

print(profile1)
```

The values are assigned based on their position:

```text
"Rahul"  → name
30       → age
"Python" → course
```

### Keyword Arguments

```python
profile2 = student_profile(
    name="Praveen",
    age=30,
    course="Python"
)

print(profile2)
```

The values are assigned using the parameter names.

### Concepts Demonstrated

* Parameters
* Arguments
* Positional arguments
* Keyword arguments
* Return values
* String formatting

---

# 12. Print vs Return

This program demonstrates the difference between using `print()` and `return`.

## Function Using `print()`

```python
def add_using_print(a, b):
    """Print the sum of two numbers."""
    
    result = a + b
    print("Inside print function:", result)
```

The result is displayed but not returned.

---

## Function Using `return`

```python
def add_using_return(a, b):
    """Return the sum of two numbers."""
    
    return a + b
```

The returned value can be stored and reused.

```python
result = add_using_return(10, 20)

new_result = result * 2

print(new_result)
```

### Why is `return` useful?

`return` allows a function's result to be:

* Stored in a variable
* Used in another calculation
* Passed to another function
* Tested in a condition
* Reused multiple times

---

# 🧠 Function Fundamentals Covered

## 1. Function Definition

A function is created using the `def` keyword.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

---

## 2. Function Call

A function is executed by calling its name.

```python
add(10, 20)
```

---

## 3. Parameters

Parameters are the variables defined in the function definition.

```python
def add(a, b):
```

Here:

```text
a
b
```

are parameters.

---

## 4. Arguments

Arguments are the actual values passed when calling a function.

```python
add(10, 20)
```

Here:

```text
10
20
```

are arguments.

---

# 📌 Positional Arguments

Values are assigned according to their position.

```python
student_profile("Rahul", 30, "Python")
```

Mapping:

```text
name   → "Rahul"
age    → 30
course → "Python"
```

---

# 📌 Keyword Arguments

Values are assigned using parameter names.

```python
student_profile(
    name="Praveen",
    age=30,
    course="Python"
)
```

The order can also be changed:

```python
student_profile(
    course="Python",
    name="Praveen",
    age=30
)
```

---

# 📌 Default Arguments

A default value is assigned to a parameter.

```python
def calculate_discount(price, discount=10):
```

If the caller does not provide `discount`, Python uses:

```text
10
```

Example:

```python
calculate_discount(1000)
```

---

# 📌 Return Values

A function can send a result back using `return`.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

The result can then be stored:

```python
result = add(10, 20)
```

---

# 📌 Docstrings

Every custom function in this task should include a short triple-quoted docstring immediately below the `def` line.

Example:

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

A docstring describes what the function does and provides built-in documentation.

---

# 📊 Requirement Mapping

| Assignment Requirement                          | Program                          | Function                                        |
| ----------------------------------------------- | -------------------------------- | ----------------------------------------------- |
| Addition                                        | `01_add_two_numbers.ipynb`       | `add()`                                         |
| Addition, subtraction, multiplication, division | `02_arithmetic_operations.ipynb` | `add()`, `subtract()`, `multiply()`, `divide()` |
| Even/Odd                                        | `03_even_or_odd.ipynb`           | `check_even_odd()`                              |
| Largest of three                                | `04_largest_of_three.ipynb`      | `largest_of_three()`                            |
| Factorial                                       | `05_factorial_function.ipynb`    | `factorial()`                                   |
| Prime check                                     | `06_prime_checker.ipynb`         | `is_prime()`                                    |
| Default argument                                | `07_calculate_discount.ipynb`    | `calculate_discount()`                          |
| List sum without `sum()`                        | `08_list_sum_function.ipynb`     | `calculate_list_sum()`                          |
| String / vowels                                 | `09_count_vowels.ipynb`          | `count_vowels()`                                |
| Palindrome                                      | `10_palindrome_function.ipynb`   | `is_palindrome()`                               |
| Positional arguments                            | `11_student_profile.ipynb`       | `student_profile()`                             |
| Keyword arguments                               | `11_student_profile.ipynb`       | `student_profile()`                             |
| `print()` vs `return`                           | `12_print_vs_return.ipynb`       | `add_using_print()`, `add_using_return()`       |

---

# ✅ Assignment Checklist

* [x] Create `add(a, b)` function
* [x] Create arithmetic operation functions
* [x] Create even/odd function
* [x] Find largest of three without `max()`
* [x] Create factorial function
* [x] Create prime-check function
* [x] Create discount function with default argument
* [x] Calculate list sum without `sum()`
* [x] Count vowels in a string
* [x] Check palindrome
* [x] Create `student_profile(name, age, course)`
* [x] Demonstrate positional arguments
* [x] Demonstrate keyword arguments
* [x] Demonstrate `print()` vs `return`
* [x] Include docstrings for custom functions
* [x] Keep problem-solving logic inside functions
* [x] Include example function calls

---

# 📁 Project Structure

```text
super30-python-functions-task-1/
│
├── 01_add_two_numbers.ipynb
├── 02_arithmetic_operations.ipynb
├── 03_even_or_odd.ipynb
├── 04_largest_of_three.ipynb
├── 05_factorial_function.ipynb
├── 06_prime_checker.ipynb
├── 07_calculate_discount.ipynb
├── 08_list_sum_function.ipynb
├── 09_count_vowels.ipynb
├── 10_palindrome_function.ipynb
├── 11_student_profile.ipynb
├── 12_print_vs_return.ipynb
└── README.md
```

---

# ▶️ How to Run

## Option 1 — Jupyter Notebook

Open any `.ipynb` file using Jupyter Notebook or JupyterLab and execute the cells sequentially.

## Option 2 — Visual Studio Code

1. Open the repository in VS Code.
2. Install the Python extension.
3. Install the Jupyter extension.
4. Open any `.ipynb` file.
5. Select a Python kernel.
6. Run the notebook cells.

---

# 🛠️ Technologies Used

* **Python 3**
* **Jupyter Notebook**
* **Visual Studio Code**
* **Git**
* **GitHub**

---

# 🎓 Learning Outcome

After completing this task, the learner should be able to confidently:

```text
Define a function
      ↓
Add parameters
      ↓
Pass arguments
      ↓
Process data inside the function
      ↓
Return a result
      ↓
Reuse the result
```

The exercises progress from simple arithmetic functions to more practical examples involving **strings, lists, default arguments, positional arguments, keyword arguments, and return values**.

---

# 📌 Submission

**Repository:** `super30-python-functions-task-1`

The repository contains all required Jupyter notebooks demonstrating the fundamentals of Python functions and reusable programming.

---

## 👨‍💻 Author

**Praveen Devisetti**

Python Learning & Practice Repository

[GitHub Repository](https://github.com/praveendevisetti0676/python_praveen)
