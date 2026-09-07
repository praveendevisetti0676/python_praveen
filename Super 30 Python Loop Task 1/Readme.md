# 🐍 Python Functions Task 1

A collection of Python programming exercises focused on **reusable programming using custom functions**.

This task introduces the core concepts required to move from writing one-time scripts to building **reusable, modular, and maintainable Python programs**.

---

## 🎯 Objective

Learn how to create and use reusable Python functions with:

* Function definitions
* Function calls
* Parameters
* Arguments
* Return values
* Variable scope
* Default arguments
* Positional arguments
* Keyword arguments
* Docstrings
* Reusable problem-solving logic

The key principle of this task is:

> **The actual problem-solving logic should exist inside the function, not outside it.**

---

# 📚 Questions / Exercises

The project contains functions covering arithmetic operations, number analysis, strings, lists, default arguments, and student information.

| #  | Exercise                    | Main Concept                      |
| -- | --------------------------- | --------------------------------- |
| 01 | ➕ Addition                  | Function, parameters, return      |
| 02 | ➖ Subtraction               | Function, parameters, return      |
| 03 | ✖️ Multiplication           | Function, parameters, return      |
| 04 | ➗ Division                  | Function, parameters, return      |
| 05 | 🔢 Even or Odd              | Conditional logic inside function |
| 06 | 🏆 Largest of Three Numbers | Parameters, conditions, return    |
| 07 | 🧮 Factorial                | Function + loop                   |
| 08 | 🔍 Prime Number Check       | Function + loop + conditions      |
| 09 | 💸 Calculate Discount       | Default argument                  |
| 10 | ➕ Sum of List               | Lists + loop + return             |
| 11 | 🔤 Count Vowels             | String processing + return        |
| 12 | 🔄 Palindrome Check         | String processing + return        |
| 13 | 🎓 Student Profile          | Positional & keyword arguments    |
| 14 | 🖨️ Print vs Return         | `print()` vs `return`             |

---

# 🧩 Core Concepts

## 1. Function Definition

A function is defined using the `def` keyword.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

Here:

* `add` → function name
* `a` and `b` → parameters
* `return` → sends the result back to the caller

---

## 2. Function Call

Defining a function does not execute it.

The function must be called:

```python
result = add(10, 20)
print(result)
```

Output:

```text
30
```

The function is defined once and can then be called multiple times.

---

# 🔑 Parameter vs Argument

Understanding the difference between a **parameter** and an **argument** is an important objective of this task.

### Parameter

A parameter is the variable written in the function definition.

```python
def add(a, b):
    return a + b
```

`a` and `b` are parameters.

### Argument

An argument is the actual value supplied when calling the function.

```python
add(10, 20)
```

`10` and `20` are arguments.

### Simple Rule

```text
Function Definition → Parameters
Function Call       → Arguments
```

---

# ↔️ Positional Arguments

Arguments can be passed according to their position.

```python
def student_profile(name, age, course):
    """Return a formatted student profile."""
    return f"Name: {name}, Age: {age}, Course: {course}"

student_profile("Praveen", 30, "Python")
```

The values are assigned based on their order.

```text
name   → "Praveen"
age    → 30
course → "Python"
```

---

# 🏷️ Keyword Arguments

Arguments can also be passed by explicitly specifying the parameter names.

```python
student_profile(
    name="Praveen",
    age=30,
    course="Python"
)
```

This is called a **keyword argument**.

The order of the arguments does not need to match the parameter order when keyword arguments are used.

---

# ⚙️ Default Arguments

A function can define a default value for a parameter.

```python
def calculate_discount(price, discount=10):
    """Return the price after applying the discount percentage."""
    return price - (price * discount / 100)
```

If the caller does not provide `discount`, Python uses the default value:

```python
calculate_discount(1000)
```

The default discount is:

```text
10%
```

A different discount can also be supplied:

```python
calculate_discount(1000, 20)
```

Here the supplied value `20` overrides the default `10`.

---

# 🔄 Return Values

The `return` statement sends a value from the function back to the caller.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

The returned value can be stored:

```python
result = add(10, 20)
```

It can also be used directly:

```python
print(add(10, 20))
```

Or used in another calculation:

```python
total = add(10, 20) * 2
```

This is one of the major advantages of using `return`.

---

# 🖨️ `print()` vs `return`

The project demonstrates an important difference between `print()` and `return`.

### Function using `print()`

```python
def add_print(a, b):
    """Print the sum of two numbers."""
    print(a + b)
```

Calling:

```python
result = add_print(10, 20)
print(result)
```

Produces:

```text
30
None
```

The function displays the result but does not send the value back to the caller.

---

### Function using `return`

```python
def add_return(a, b):
    """Return the sum of two numbers."""
    return a + b
```

Calling:

```python
result = add_return(10, 20)
print(result)
```

Produces:

```text
30
```

The value can now be reused.

For example:

```python
result = add_return(10, 20)

double = result * 2
print(double)
```

Output:

```text
60
```

### Key Difference

```text
print() → displays a value
return  → sends a value back to the caller
```

Therefore, **`return` is generally more useful when building reusable functions**.

---

# 📋 Function Requirements

Every custom function in this project includes a **docstring** explaining its purpose.

Example:

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

The docstring makes the function easier to understand and maintain.

---

# 🧮 Functions Covered

## Arithmetic Functions

The project implements separate functions for:

```text
Addition
Subtraction
Multiplication
Division
```

Each function receives values through parameters and returns the calculated result.

---

## 🔢 Even or Odd

A function determines whether a number is even or odd.

Example concept:

```python
def check_even_odd(number):
    """Return whether a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    return "Odd"
```

---

## 🏆 Largest of Three Numbers

A function determines the largest of three numbers **without using `max()`**.

The comparison logic is implemented inside the function itself.

---

## 🧮 Factorial

A factorial function calculates the factorial of a number.

For example:

```text
5! = 5 × 4 × 3 × 2 × 1
```

Therefore:

```text
5! = 120
```

The calculation logic is contained inside the function.

---

## 🔍 Prime Number Check

A function determines whether a number is prime.

Example:

```text
2 → Prime
3 → Prime
4 → Not Prime
5 → Prime
```

The function contains the number-checking logic rather than performing the logic outside the function.

---

## 💸 Discount Calculator

The required function is:

```python
def calculate_discount(price, discount=10):
    """Return the price after applying the discount percentage."""
```

The default discount is **10%**.

The function also allows the caller to provide a different discount percentage.

---

## ➕ List Sum Without `sum()`

A function accepts a list and calculates its total **without using Python's built-in `sum()` function**.

The calculation is performed using iteration inside the function.

---

## 🔤 Vowel Counter

A function accepts a string and returns the number of vowels.

Typical vowels checked are:

```text
a, e, i, o, u
```

The function demonstrates:

* String iteration
* Conditional checking
* Counters
* Return values

---

## 🔄 Palindrome Checker

A function accepts a string and determines whether it is a palindrome.

Examples:

```text
madam → Palindrome
level → Palindrome
python → Not a palindrome
```

---

# 🎓 Student Profile

A function accepts:

```text
name
age
course
```

and returns a formatted student profile.

Example:

```python
def student_profile(name, age, course):
    """Return a formatted student profile."""
    return f"Name: {name}\nAge: {age}\nCourse: {course}"
```

The function is called using both:

### Positional Arguments

```python
student_profile("Praveen", 30, "Python")
```

### Keyword Arguments

```python
student_profile(
    name="Praveen",
    age=30,
    course="Python"
)
```

This demonstrates the difference between the two calling styles.

---

# 📂 Recommended Project Structure

```text
super30-python-functions-task-1/
│
├── 01_addition.ipynb
├── 02_subtraction.ipynb
├── 03_multiplication.ipynb
├── 04_division.ipynb
├── 05_even_odd.ipynb
├── 06_largest_of_three.ipynb
├── 07_factorial.ipynb
├── 08_prime_check.ipynb
├── 09_calculate_discount.ipynb
├── 10_list_sum.ipynb
├── 11_count_vowels.ipynb
├── 12_palindrome.ipynb
├── 13_student_profile.ipynb
├── 14_print_vs_return.ipynb
└── README.md
```

> The exact notebook names may be adjusted according to the final implementation.

---

# 🚫 Important Submission Requirement

The assignment specifically requires that the **actual problem-solving logic must exist inside the functions**.

### ❌ Avoid

```python
numbers = [10, 20, 30]

total = 0
for number in numbers:
    total += number

def calculate_total(numbers):
    return total
```

The logic is outside the function.

### ✅ Preferred

```python
def calculate_total(numbers):
    """Return the total of all numbers in a list."""
    total = 0

    for number in numbers:
        total += number

    return total
```

Now the function contains the complete problem-solving logic and can be reused with different inputs.

---

# 🧱 Reusable Programming Principle

The overall design principle of this project is:

```text
Input
  │
  ▼
Function
  │
  ├── Parameters
  ├── Problem-solving logic
  └── Return value
  │
  ▼
Reusable Result
```

Instead of writing the same logic repeatedly, we define it once inside a function and call it whenever required.

---

# 📈 Learning Progression

The exercises progress from simple functions to more reusable programming concepts:

```text
Function Definition
        │
        ▼
Function Call
        │
        ▼
Parameters & Arguments
        │
        ▼
Return Values
        │
        ▼
Conditional Logic
        │
        ▼
Loops Inside Functions
        │
        ▼
Default Arguments
        │
        ▼
Positional & Keyword Arguments
        │
        ▼
Reusable Problem Solving
        │
        ▼
Modular Python Programs
```

---

# 🎥 YouTube Explanation

The accompanying YouTube explanation should cover the following concepts:

### Function Fundamentals

* What is a function?
* Why do we use functions?
* Function definition
* Function call

### Function Inputs

* Parameter
* Argument
* Positional argument
* Keyword argument
* Default argument

### Function Outputs

* `return`
* Difference between `print()` and `return`
* Why `return` is useful for reusable programming

### Practical Demonstrations

The explanation should demonstrate these concepts using the functions created in this project.

---

# 🛠️ Technologies Used

* 🐍 Python 3
* 📓 Jupyter Notebook
* 💻 Visual Studio Code
* 🌐 GitHub

---

# 📦 Submission

**GitHub Repository:**

```text
super30-python-functions-task-1
```

The repository should contain:

* All required Python/Jupyter exercises
* Custom functions for each problem
* Docstrings for every custom function
* Actual problem-solving logic inside the functions
* Examples of positional and keyword arguments
* Examples demonstrating `print()` vs `return`
* `README.md`

---

# 🎓 Key Takeaway

The most important lesson from this task is:

> **A good function encapsulates a specific piece of logic, accepts input through parameters, performs the required processing, and returns a useful result.**

Functions help transform Python programs from repetitive scripts into **reusable, modular, readable, and maintainable code**.

---

## 👨‍💻 Author

**Praveen Devisetti**

Python learning exercises and programming projects.

---

⭐ **Define once. Reuse everywhere.**
