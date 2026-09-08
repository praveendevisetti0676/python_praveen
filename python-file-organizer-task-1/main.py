from pathlib import Path

import file_organizer

import file_organizer.logger


def organize_folder(source_folder):
    source_folder = Path(source_folder)

    if not source_folder.exists():
        message = f"Source folder does not exist: {source_folder}"
        file_organizer.logger.log_error(message)
        print("Error:", message)
        return

    if not source_folder.is_dir():
        message = f"Path is not a folder: {source_folder}"
        file_organizer.logger.log_error(message)
        print("Error:", message)
        return

    files = list(source_folder.iterdir())

    if not files:
        print("No files found in the folder.")
        return

    for file_path in files:

        if not file_path.is_file():
            continue

        try:
            category = file_organizer.detect_file_category(file_path)

            destination_folder = source_folder / category

            file_organizer.move_file(
                file_path,
                destination_folder
            )

            print(
                f"Moved: {file_path.name} "
                f"→ {category}/"
            )

        except UnsupportedFileError as error:
            file_organizer.logger.log_error(str(error))
            print(
                f"Unsupported: {file_path.name}"
            )

        except PermissionError:
            print(
                f"Permission denied: {file_path.name}"
            )

        except FileNotFoundError:
            print(
                f"File not found: {file_path.name}"
            )

        except ValueError as error:
            file_organizer.logger.log_error(str(error))
            print(
                f"Invalid file: {file_path.name}"
            )

        except OSError as error:
            file_organizer.logger.log_error(str(error))
            print(
                f"File operation failed: {file_path.name}"
            )


def main():

    print("=" * 45)
    print("       PYTHON FILE ORGANIZER")
    print("=" * 45)

    folder = input(
        "Enter the folder path to organize: "
    ).strip()
    print("origin folder name", folder)
    organize_folder(folder)


if __name__ == "__main__":
    main()