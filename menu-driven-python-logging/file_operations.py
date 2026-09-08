from pathlib import Path

from exceptions import FileOperationError


def read_file(filename, logger):
    """Read and display the contents of a file."""

    logger.debug(
        f"Reading file: {filename}"
    )

    path = Path(filename)

    try:

        if not path.exists():

            logger.error(
                f"File could not be opened: {filename}"
            )

            raise FileOperationError(
                f"File does not exist: {filename}"
            )

        content = path.read_text(
            encoding="utf-8"
        )

        if not content.strip():

            logger.warning(
                f"File was empty: {filename}"
            )

            print("Warning: File is empty.")

            return

        logger.info(
            f"File read successfully: {filename}"
        )

        print("\nFile Content")
        print("-" * 40)
        print(content)
        print("-" * 40)

    except FileOperationError:
        raise

    except PermissionError as error:

        logger.error(
            f"Permission denied: {filename}"
        )

        raise FileOperationError(
            "Permission denied while reading file."
        ) from error

    except OSError as error:

        logger.error(
            f"File could not be opened: {filename}"
        )

        raise FileOperationError(
            "File could not be opened."
        ) from error


def write_file(filename, content, logger):
    """Write content to a file."""

    logger.debug(
        f"Writing to file: {filename}"
    )

    path = Path(filename)

    try:

        path.write_text(
            content,
            encoding="utf-8"
        )

        logger.info(
            f"File written successfully: {filename}"
        )

        print(
            "File written successfully."
        )

    except PermissionError as error:

        logger.error(
            f"Permission denied while writing: {filename}"
        )

        raise FileOperationError(
            "Permission denied while writing file."
        ) from error

    except OSError as error:

        logger.error(
            f"File could not be written: {filename}"
        )

        raise FileOperationError(
            "File could not be written."
        ) from error