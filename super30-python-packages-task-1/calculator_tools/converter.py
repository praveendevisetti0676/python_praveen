from .exceptions import InvalidOperationError


def _validate_number(value):
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError("Value must be a number.")


def celsius_to_fahrenheit(celsius):
    _validate_number(celsius)

    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    _validate_number(fahrenheit)

    return (fahrenheit - 32) * 5 / 9


def kilometers_to_miles(kilometers):
    _validate_number(kilometers)

    if kilometers < 0:
        raise ValueError("Distance cannot be negative.")

    return kilometers * 0.621371


def miles_to_kilometers(miles):
    _validate_number(miles)

    if miles < 0:
        raise ValueError("Distance cannot be negative.")

    return miles * 1.60934


def convert(value, conversion):
    conversions = {
        "c_to_f": celsius_to_fahrenheit,
        "f_to_c": fahrenheit_to_celsius,
        "km_to_miles": kilometers_to_miles,
        "miles_to_km": miles_to_kilometers
    }

    if conversion not in conversions:
        raise InvalidOperationError(
            f"Unsupported conversion: {conversion}"
        )

    return conversions[conversion](value)