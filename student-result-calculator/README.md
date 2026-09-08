# Student Result Calculator

A Python-based **Student Result Calculator** that reads student information and marks for five subjects, calculates the total, percentage, grade, and pass/fail status, and handles invalid input using **custom exceptions and logging**.

The project is designed using a **modular Python architecture**, where student input, result calculations, exception definitions, and logging configuration are separated into different modules.

---

## 📌 Project Objective

The objective of this project is to create a Python program that:

* Reads student details.
* Reads marks for 5 subjects.
* Calculates total marks.
* Calculates percentage.
* Determines the grade.
* Determines Pass/Fail status.
* Validates marks between `0` and `100`.
* Handles non-numeric input.
* Handles missing student information.
* Handles calculation errors.
* Uses custom exceptions.
* Logs errors into a log file.
* Continues processing the remaining students when one student has invalid data.
* Uses separate Python modules for different responsibilities.

---

## 📂 Project Structure

```text
student-result-calculator/
│
├── main.py
├── student_operations.py
├── result_calculator.py
├── exceptions.py
├── logger_config.py
├── result_calculator.log
└── README.md
```

---

## 🧩 Module Responsibilities

### 1. `main.py`

This is the **main entry point** of the application.

Responsibilities:

* Starts the application.
* Reads the number of students.
* Processes each student.
* Calls functions from other modules.
* Handles exceptions.
* Logs errors.
* Continues processing after an error.

---

### 2. `student_operations.py`

Handles student-related input and validation.

Functions:

```python
get_number_of_students()
get_student_info()
get_marks()
```

Responsibilities:

* Read number of students.
* Read student name.
* Read student ID.
* Read marks for five subjects.
* Validate numeric marks.
* Validate marks between `0` and `100`.
* Detect missing student information.

---

### 3. `result_calculator.py`

Contains the result calculation logic.

Functions:

```python
calculate_total()
calculate_percentage()
calculate_grade()
calculate_pass_fail()
```

Responsibilities:

* Calculate total marks.
* Calculate percentage.
* Calculate grade.
* Determine Pass/Fail status.

---

### 4. `exceptions.py`

Contains custom exception classes.

```python
class InvalidMarksError(Exception):
    """Raised when marks are outside the range 0 to 100."""


class MissingStudentInfoError(Exception):
    """Raised when required student information is missing."""
```

Custom exceptions make the application easier to understand and maintain.

---

### 5. `logger_config.py`

Contains the logging configuration.

The application writes errors and other log messages to:

```text
result_calculator.log
```

Example log entry:

```text
2026-09-08 10:15:20,123 - ERROR - Invalid marks: Marks must be between 0 and 100. Received: 120.0
```

---

## 📊 Grade Calculation

The following grading system is used:

| Percentage | Grade |
| ---------: | :---- |
|   90 – 100 | A+    |
|    80 – 89 | A     |
|    70 – 79 | B     |
|    60 – 69 | C     |
|    50 – 59 | D     |
|   Below 50 | F     |

---

## ✅ Pass/Fail Criteria

A student receives **PASS** when every subject has at least **35 marks**.

For example:

```text
80, 75, 65, 70, 85
```

Result:

```text
PASS
```

If even one subject is below 35:

```text
80, 75, 30, 70, 85
```

Result:

```text
FAIL
```

---

## ⚠️ Error Handling

The application handles several types of errors.

### 1. Invalid Marks

Marks must be between `0` and `100`.

Example:

```text
Enter marks for subject 1: 120
```

Output:

```text
Error: Marks must be between 0 and 100.
```

The error is also written to the log file.

---

### 2. Non-Numeric Marks

Example:

```text
Enter marks for subject 1: abc
```

Output:

```text
Error: Marks must be numeric.
```

---

### 3. Missing Student Information

If the student name or ID is empty:

```text
Error: Student name is required.
```

or:

```text
Error: Student ID is required.
```

---

### 4. Invalid Number of Students

The number of students must be a positive integer.

Example:

```text
Enter number of students: abc
```

Output:

```text
Error: Number of students must be a valid integer.
```

---

### 5. Calculation Errors

The program also handles `ZeroDivisionError` so that unexpected calculation problems do not terminate the complete application.

---

## 🔄 Continue Processing After Errors

One of the important requirements of this project is that the application **must not stop when one student has invalid data**.

For example:

```text
--- Student 1 ---

Enter student name: Rahul
Enter student ID: S101
Enter marks for subject 1: 120

Error: Marks must be between 0 and 100.
Finished processing student 1.

--- Student 2 ---

Enter student name: Anil
Enter student ID: S102
...
```

Student 1 has an invalid mark, but the program continues with Student 2.

This is achieved using exception handling inside the student-processing loop:

```python
for student_number in range(
    1,
    number_of_students + 1
):

    try:
        process_student()

    except InvalidMarksError as error:
        logger.error(
            f"Invalid marks: {error}"
        )

        print(
            f"Error: {error}"
        )
```

---

## 🛠️ Technologies Used

* **Python 3**
* Python Functions
* Python Modules
* Exception Handling
* Custom Exceptions
* Logging
* Input Validation
* Loops
* Conditional Statements
* String Formatting

---

## ▶️ How to Run

### Step 1: Open the project folder

```powershell
cd "C:\Users\pdevi\Downloads\Super 30 exmples\student-result-calculator"
```

### Step 2: Run the program

```powershell
python main.py
```

If multiple Python versions are installed, you can also use:

```powershell
py main.py
```

---

## 🧪 Example Execution

```text
Enter number of students: 1

--- Student 1 ---

Enter student name: Rahul
Enter student ID: S101
Enter marks for subject 1: 85
Enter marks for subject 2: 78
Enter marks for subject 3: 92
Enter marks for subject 4: 88
Enter marks for subject 5: 80
```

Output:

```text
=============================================
             STUDENT RESULT
=============================================
Name       : Rahul
Student ID : S101
Total      : 423.00
Percentage : 84.60%
Grade      : A
Status     : PASS
=============================================
Finished processing student 1.
```

---

## 📝 Logging

The application uses Python's built-in `logging` module.

Errors are recorded in:

```text
result_calculator.log
```

Example:

```text
2026-09-08 10:20:15 - ERROR - Invalid marks: Marks must be between 0 and 100. Received: 120.0
```

Logging provides a history of errors without requiring the user to manually track them.

---

## 🧠 Python Concepts Demonstrated

This project demonstrates several important Python concepts.

### Functions

Functions are used to separate individual operations:

```python
def calculate_total(marks):
    return sum(marks)
```

### Modules

The program is divided into multiple modules:

```text
student_operations.py
result_calculator.py
exceptions.py
logger_config.py
```

This improves code organization and maintainability.

### Custom Exceptions

The project defines application-specific exceptions:

```python
class InvalidMarksError(Exception):
    pass
```

### Exception Handling

Different errors are handled separately:

```python
try:
    process_student()

except InvalidMarksError as error:
    ...
```

### Logging

Python's `logging` module is used to record errors:

```python
logger.error(
    f"Invalid marks: {error}"
)
```

### Input Validation

User input is validated before processing.

### Loops

A `for` loop is used to process multiple students:

```python
for student_number in range(
    1,
    number_of_students + 1
):
    process_student()
```

---

## 🧪 Testing Checklist

The following scenarios should be tested:

* [ ] Valid student information
* [ ] Multiple students
* [ ] Empty student name
* [ ] Empty student ID
* [ ] Non-numeric marks
* [ ] Marks below `0`
* [ ] Marks above `100`
* [ ] Student with marks below `35`
* [ ] Student with all subjects above `35`
* [ ] Invalid number of students
* [ ] Error logging
* [ ] Continue processing after an invalid student
* [ ] Correct total
* [ ] Correct percentage
* [ ] Correct grade
* [ ] Correct Pass/Fail status

---

## 🎯 Learning Outcomes

After completing this project, you will understand how to:

1. Create a modular Python application.
2. Separate input and calculation logic.
3. Create custom exception classes.
4. Validate user input.
5. Handle different types of exceptions.
6. Use Python logging.
7. Continue application execution after errors.
8. Organize a Python project into multiple modules.
9. Build reusable functions.
10. Write maintainable Python code.

---

## 📌 Key Design Principle

The project follows the principle of **separation of concerns**.

```text
                 main.py
                    │
        ┌───────────┼────────────┐
        │           │            │
        ▼           ▼            ▼
 student_operations  result_calculator
        │           │
        │           │
        ▼           ▼
     Input       Calculations
        │           │
        └─────┬─────┘
              │
              ▼
         exceptions.py
              │
              ▼
       logger_config.py
              │
              ▼
     result_calculator.log
```

Each module has a specific responsibility instead of putting the complete application into one Python file.

---

## 👨‍💻 Author

**Praveen Devisetti**

Python Modular Programming Exercise

---

## 📄 License

This project is created for **learning and educational purposes**.
