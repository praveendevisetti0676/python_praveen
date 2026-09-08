from pathlib import Path

from .exceptions import UnsupportedFileError


FILE_CATEGORIES = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",

    ".txt": "Text",
    ".md": "Text",

    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".ppt" : "Documents",
    ".pptx": "Documents"

    ".csv": "Data",
    ".xlsx": "Data",
    ".xls": "Data",
    ".json": "Data",

    ".mp3": "Audio",
    ".wav": "Audio",

    ".mp4": "Videos",
    ".avi": "Videos"
}


def detect_file_category(file_path):
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"File does not exist: {file_path}"
        )

    if not file_path.is_file():
        raise ValueError(
            f"Path is not a file: {file_path}"
        )

    extension = file_path.suffix.lower()

    if extension not in FILE_CATEGORIES:
        raise UnsupportedFileError(
            f"Unsupported file type: {extension}"
        )

    return FILE_CATEGORIES[extension]