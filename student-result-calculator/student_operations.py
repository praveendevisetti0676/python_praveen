from exceptions import (
    InvalidMarksError,
    MissingStudentInfoError
)


def get_number_of_students():
    """Read and validate the number of students."""

    value = input("Enter number of students: ").strip()

    try:
        number = int(value)

    except ValueError:
        raise ValueError(
            "Number of students must be a valid integer."
        )

    if number <= 0:
        raise ValueError(
            "Number of students must be greater than zero."
        )

    return number


def get_student_info():
    """Read and validate student name and ID."""

    name = input("Enter student name: ").strip()

    student_id = input("Enter student ID: ").strip()

    if not name:
        raise MissingStudentInfoError(
            "Student name is required."
        )

    if not student_id:
        raise MissingStudentInfoError(
            "Student ID is required."
        )

    return name, student_id


def get_marks():
    """Read and validate marks for five subjects."""

    marks = []

    for subject_number in range(1, 6):

        value = input(
            f"Enter marks for subject {subject_number}: "
        ).strip()

        try:
            mark = float(value)

        except ValueError:
            raise ValueError(
                f"Marks must be numeric. Received: {value}"
            )

        if mark < 0 or mark > 100:
            raise InvalidMarksError(
                f"Marks must be between 0 and 100. "
                f"Received: {mark}"
            )

        marks.append(mark)

    return marks