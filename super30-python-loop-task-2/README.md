
# 🐍 Python Loop Task 2

A collection of **Python loop-based programming exercises** designed to strengthen understanding of `for` loops, `while` loops, `break`, `continue`, `for-else`, `enumerate()`, nested loops, pattern printing, and basic number analysis.

These exercises focus on solving small programming problems using **iteration and logical thinking**.

---

## 🎯 Learning Objectives

The goal of this task is to build confidence with Python loops and understand how different loop-control techniques can be applied to practical problems.

By completing these exercises, you will practice:

* ✅ `for` loops
* ✅ `while` loops
* ✅ `break`
* ✅ `continue`
* ✅ `for-else`
* ✅ `enumerate()`
* ✅ Nested loops
* ✅ Number analysis
* ✅ Conditional logic inside loops
* ✅ Pattern printing
* ✅ Counting and filtering values
* ✅ Finding unique elements
* ✅ Prime-number logic

---

# 📚 Exercises

| #  | Exercise                                 | Main Concept              |
| -- | ---------------------------------------- | ------------------------- |
| 01 | ⏭️ Skip Numbers Divisible by 5           | `continue`                |
| 02 | 🛑 Break on Number Divisible by 7 and 11 | `break`                   |
| 03 | 🔍 Search Number Using `for-else`        | `for-else`                |
| 04 | 🔢 Enumerate Names                       | `enumerate()`             |
| 05 | ⭐ Increasing Star Pattern                | Nested loops              |
| 06 | ⭐ Decreasing Star Pattern                | Nested loops              |
| 07 | ✖️ Multiplication Tables 1 to 10         | Nested loops              |
| 08 | 🔢 Numbers Divisible by 3 and 5          | Conditions + loops        |
| 09 | 🧩 Unique Elements                       | Lists + loops             |
| 10 | 📊 Count Positive, Negative & Zero       | Conditions + loops        |
| 11 | 🔎 Check Prime Number                    | Loop + mathematical logic |
| 12 | 🔢 Prime Numbers from 1 to 100           | Nested/repeated iteration |

---

# 📂 Project Structure

```text
super30-python-loop-task-2/
│
├── 01_skip_divisible_by_5.ipynb
├── 02_break_divisible_by_7_and_11.ipynb
├── 03_search_number_for_else.ipynb
├── 04_enumerate_names.ipynb
├── 05_increasing_star_pattern.ipynb
├── 06_decreasing_star_pattern.ipynb
├── 07_multiplication_tables_1_to_10.ipynb
├── 08_divisible_by_3_and_5.ipynb
├── 09_unique_elements.ipynb
├── 10_count_positive_negative_zero.ipynb
├── 11_check_prime.ipynb
├── 12_prime_numbers_1_to_100.ipynb
├── positive_negative.ipynb
└── README.md
```

---

# 🧠 Concepts Covered

## 1. `continue`

The `continue` statement skips the current iteration and moves to the next iteration of the loop.

Example:

```python
for number in range(1, 21):
    if number % 5 == 0:
        continue
    print(number)
```

This exercise demonstrates how `continue` can be used to **skip unwanted values without stopping the loop**.

---

## 2. `break`

The `break` statement immediately terminates a loop.

Example:

```python
for number in range(1, 101):
    if number % 7 == 0 and number % 11 == 0:
        break
```

This demonstrates how `break` can be used when a required condition has been reached.

---

## 3. `for-else`

Python's `for-else` construct is useful when searching for an item.

```python
for number in numbers:
    if number == target:
        print("Found")
        break
else:
    print("Not found")
```

The `else` block executes only when the loop completes **without encountering a `break`**.

---

## 4. `enumerate()`

`enumerate()` provides both the index and value while iterating over a sequence.

```python
names = ["Praveen", "Rahul", "Anita"]

for index, name in enumerate(names):
    print(index, name)
```

This is cleaner than manually maintaining a counter variable.

---

## 5. Nested Loops

A loop inside another loop is called a **nested loop**.

Nested loops are useful for:

* Pattern printing
* Tables
* Matrix operations
* Comparing multiple values
* Repeated calculations

Example:

```python
for row in range(1, 6):
    for column in range(row):
        print("*", end=" ")
    print()
```

---

# ⭐ Pattern Printing

The project includes both increasing and decreasing star patterns.

### Increasing Pattern

```text
*
* *
* * *
* * * *
* * * * *
```

### Decreasing Pattern

```text
* * * * *
* * * *
* * *
* *
*
```

These exercises help develop an understanding of **nested loops and iteration control**.

---

# ✖️ Multiplication Tables

The multiplication-table exercise demonstrates how nested loops can be used to generate multiple tables.

For example:

```text
1 x 1 = 1
1 x 2 = 2
...

10 x 1 = 10
10 x 2 = 20
...
```

This is a practical example of combining:

* Nested loops
* Arithmetic operations
* Formatted output

---

# 🔢 Number Analysis

Several exercises focus on analyzing numbers using loops and conditions.

Examples include:

### Divisibility

Finding numbers divisible by both **3 and 5**.

```python
if number % 3 == 0 and number % 5 == 0:
    print(number)
```

### Positive / Negative / Zero

Classifying numbers into:

* Positive
* Negative
* Zero

### Prime Numbers

Determining whether a number is prime and generating prime numbers between **1 and 100**.

---

# 🧩 Unique Elements

The unique-elements exercise demonstrates how loops can be used to identify values that occur only once or eliminate duplicate values.

This provides practice with:

* Lists
* Membership checking
* Iteration
* Conditional logic

---

# 🔎 Prime Number Logic

A prime number is a number greater than `1` that has exactly two factors:

```text
1 and itself
```

Examples:

```text
2, 3, 5, 7, 11, 13, 17, ...
```

The project contains two related exercises:

1. Check whether a given number is prime.
2. Find prime numbers between 1 and 100.

These exercises reinforce the relationship between **loops, conditions, and mathematical reasoning**.

---

# 🚀 How to Run

## Using Jupyter Notebook

Install Jupyter Notebook:

```bash
pip install notebook
```

Start Jupyter:

```bash
jupyter notebook
```

Open the required `.ipynb` file and run the cells sequentially.

---

## Using Visual Studio Code

1. Install Python 3.
2. Install [Visual Studio Code](https://code.visualstudio.com/).
3. Install the Python extension.
4. Open the project folder.
5. Open any `.ipynb` file.
6. Select a Python kernel.
7. Run the cells.

---

# 🛠️ Technologies Used

* 🐍 Python 3
* 📓 Jupyter Notebook
* 💻 Visual Studio Code
* 🌐 GitHub
* 🔧 Git

---

# 📈 Learning Progression

The exercises build progressively from basic loop control to more complex iteration problems.

```text
Basic Loop
    │
    ▼
continue
    │
    ▼
break
    │
    ▼
for-else
    │
    ▼
enumerate()
    │
    ▼
Nested Loops
    │
    ▼
Pattern Printing
    │
    ▼
Number Analysis
    │
    ▼
List Processing
    │
    ▼
Prime Number Analysis
```

---

# 📋 Exercise Links

1. [01 — Skip Divisible by 5](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-loop-task-2/01_skip_divisible_by_5.ipynb)
2. [02 — Break Divisible by 7 and 11](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-loop-task-2/02_break_divisible_by_7_and_11.ipynb)
3. [03 — Search Number Using for-else](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-loop-task-2/03_search_number_for_else.ipynb)
4. [04 — Enumerate Names](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-loop-task-2/04_enumerate_names.ipynb)
5. [05 — Increasing Star Pattern](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-loop-task-2/05_increasing_star_pattern.ipynb)
6. [06 — Decreasing Star Pattern](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-loop-task-2/06_decreasing_star_pattern.ipynb)
7. [07 — Multiplication Tables 1 to 10](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-loop-task-2/07_multiplication_tables_1_to_10.ipynb)
8. [08 — Divisible by 3 and 5](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-loop-task-2/08_divisible_by_3_and_5.ipynb)
9. [09 — Unique Elements](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-loop-task-2/09_unique_elements.ipynb)
10. [10 — Count Positive, Negative and Zero](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-loop-task-2/10_count_positive_negative_zero.ipynb)
11. [11 — Check Prime](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-loop-task-2/11_check_prime.ipynb)
12. [12 — Prime Numbers 1 to 100](https://github.com/praveendevisetti0676/python_praveen/blob/main/super30-python-loop-task-2/12_prime_numbers_1_to_100.ipynb)

---

# 🎓 Key Takeaway

The central theme of this project is:

> **Use loops to repeat, conditions to decide, and loop-control statements to control execution.**

By completing these exercises, the learner builds a strong foundation for writing Python programs that process **numbers, lists, strings, and repeated operations** efficiently.

---

## 👨‍💻 Author

**Praveen Devisetti**

Python learning exercises and programming projects.

---

⭐ **Keep practicing — every loop builds better programming logic!**
