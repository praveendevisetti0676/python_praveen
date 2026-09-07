def calculate_average(numbers):
    if not isinstance(numbers, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")

    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of an empty list.")

    for number in numbers:
        if not isinstance(number, (int, float)) or isinstance(number, bool):
            raise TypeError("All values must be numbers.")

    return sum(numbers) / len(numbers)