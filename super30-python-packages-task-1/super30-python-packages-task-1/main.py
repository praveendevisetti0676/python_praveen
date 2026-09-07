from calculator_tools import (
    add,
    subtract,
    multiply,
    divide,
    percentage,
    calculate_average,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kilometers_to_miles,
    miles_to_kilometers,
    InvalidOperationError
)
def main():
    print("================================")
    print("   CALCULATOR TOOLS DEMO")
    print("================================")

    # Arithmetic
    print("\n--- Arithmetic ---")

    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))
    print("Multiplication:", multiply(10, 5))
    print("Division:", divide(10, 5))

    # Percentage
    print("\n--- Percentage ---")

    print("10% of 500:", percentage(500, 10))

    # Statistics
    print("\n--- Statistics ---")

    numbers = [10, 20, 30, 40, 50]

    print("Numbers:", numbers)
    print("Average:", calculate_average(numbers))

    # Temperature conversion
    print("\n--- Temperature Conversion ---")

    print(
        "25 Celsius to Fahrenheit:",
        celsius_to_fahrenheit(25)
    )

    print(
        "77 Fahrenheit to Celsius:",
        fahrenheit_to_celsius(77)
    )

    # Unit conversion
    print("\n--- Unit Conversion ---")

    print(
        "10 Kilometers to Miles:",
        kilometers_to_miles(10)
    )

    print(
        "10 Miles to Kilometers:",
        miles_to_kilometers(10)
    )

    # Error handling
    print("\n--- Error Handling ---")

    try:
        divide(10, 0)
    except ZeroDivisionError as error:
        print("Error:", error)

    try:
        add(10, "20")
    except TypeError as error:
        print("Error:", error)

    try:
        calculate_average([])
    except ValueError as error:
        print("Error:", error)

    try:
        from calculator_tools.arithmetic import calculate

        calculate("power", 10, 2)

    except InvalidOperationError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()