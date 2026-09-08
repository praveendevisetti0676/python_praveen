def calculate_total(marks):
    """Calculate the total marks."""
    return sum(marks)


def calculate_percentage(total, number_of_subjects=5):
    """Calculate percentage from total marks."""

    if number_of_subjects <= 0:
        raise ZeroDivisionError(
            "Number of subjects must be greater than zero."
        )

    maximum_marks = number_of_subjects * 100

    return (total / maximum_marks) * 100


def calculate_grade(percentage):
    """Calculate grade based on percentage."""

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"


def calculate_pass_fail(marks):
    """Return PASS if every subject has at least 35 marks."""

    if all(mark >= 35 for mark in marks):
        return "PASS"

    return "FAIL"