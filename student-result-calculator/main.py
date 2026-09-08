from student_operations import (
    get_number_of_students,
    get_student_info,
    get_marks
)

from result_calculator import (
    calculate_total,
    calculate_percentage,
    calculate_grade,
    calculate_pass_fail
)

from exceptions import (
    InvalidMarksError,
    MissingStudentInfoError
)

from logger_config import get_logger


logger = get_logger()


def process_student():
    """Read student data and calculate the complete result."""

    name, student_id = get_student_info()

    marks = get_marks()

    total = calculate_total(marks)

    percentage = calculate_percentage(total)

    grade = calculate_grade(percentage)

    status = calculate_pass_fail(marks)

    print("\n" + "=" * 45)
    print("             STUDENT RESULT")
    print("=" * 45)

    print(f"Name       : {name}")
    print(f"Student ID : {student_id}")
    print(f"Total      : {total:.2f}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")
    print(f"Status     : {status}")

    print("=" * 45)


def main():
    """Process multiple students and handle errors."""

    try:
        number_of_students = get_number_of_students()

    except ValueError as error:
        logger.error(
            f"Invalid number of students: {error}"
        )

        print(
            f"Error: {error}"
        )

        return

    for student_number in range(1,number_of_students + 1):

        print(
            f"\n--- Student {student_number} ---"
        )

        try:
            process_student()

        except MissingStudentInfoError as error:
            logger.error(
                f"Missing student information: {error}"
            )

            print(
                f"Error: {error}"
            )

        except InvalidMarksError as error:
            logger.error(
                f"Invalid marks: {error}"
            )

            print(
                f"Error: {error}"
            )

        except ValueError as error:
            logger.error(
                f"Invalid input: {error}"
            )

            print(
                f"Error: {error}"
            )

        except ZeroDivisionError as error:
            logger.error(
                f"Calculation error: {error}"
            )

            print(
                f"Calculation error: {error}"
            )

        except PermissionError as error:
            logger.error(
                f"Permission error: {error}"
            )

            print(
                f"Permission error: {error}"
            )

        except OSError as error:
            logger.error(
                f"File or operating system error: {error}"
            )

            print(
                f"File operation error: {error}"
            )

        except Exception as error:
            logger.exception(
                f"Unexpected error: {error}"
            )

            print(
                f"Unexpected error: {error}"
            )

        print(
            f"Finished processing student {student_number}."
        )


if __name__ == "__main__":
    main()