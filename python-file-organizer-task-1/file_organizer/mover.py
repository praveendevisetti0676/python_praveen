from pathlib import Path
import shutil

from .logger import log_success, log_error


def get_unique_destination(destination):
    destination = Path(destination)

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            f"{destination.stem}_{counter}"
            f"{destination.suffix}"
        )

        new_destination = destination.with_name(new_name)

        if not new_destination.exists():
            return new_destination

        counter += 1


def move_file(source, destination_folder):
    source = Path(source)
    destination_folder = Path(destination_folder)

    try:
        if not source.exists():
            raise FileNotFoundError(
                f"File does not exist: {source}"
            )

        if not source.is_file():
            raise ValueError(
                f"Source is not a file: {source}"
            )

        destination_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        destination = destination_folder / source.name

        if destination.exists():
            destination = get_unique_destination(destination)

            log_success(
                f"Duplicate detected. Renamed destination to "
                f"{destination.name}"
            )

        shutil.move(str(source), str(destination))

        log_success(
            f"Moved {source.name} to "
            f"{destination_folder.name}"
        )

        return destination

    except PermissionError as error:
        log_error(
            f"Permission denied while moving "
            f"{source}: {error}"
        )
        raise

    except FileNotFoundError as error:
        log_error(
            f"File not found: {error}"
        )
        raise

    except OSError as error:
        log_error(
            f"File operation failed: {error}"
        )
        raise