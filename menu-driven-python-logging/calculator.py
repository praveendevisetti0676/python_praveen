from exceptions import CalculationError


def calculate(number1, number2, operation, logger):
    """Perform the requested calculation."""

    logger.debug(
        f"Calculation requested: "
        f"{number1} {operation} {number2}"
    )

    try:

        if operation == "+":

            result = number1 + number2

        elif operation == "-":

            result = number1 - number2

        elif operation == "*":

            result = number1 * number2

        elif operation == "/":

            if number2 == 0:

                logger.error(
                    "Division by zero attempted"
                )

                raise CalculationError(
                    "Cannot divide by zero."
                )

            result = number1 / number2

        else:

            logger.warning(
                f"Invalid operation: {operation}"
            )

            raise CalculationError(
                "Invalid operation."
            )

        logger.info(
            "Calculation completed"
        )

        return result

    except CalculationError:
        raise

    except Exception as error:

        logger.exception(
            f"Unexpected calculation error: {error}"
        )

        raise CalculationError(
            "Calculation could not be completed."
        )