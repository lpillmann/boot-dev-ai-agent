import os

from functions.config import MAX_CHARS_FROM_FILE, MAX_CHARS_ERROR_MSG_TEMPLATE


def get_file_content(working_directory: str, file_path: str):
    full_path_working_dir = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not full_path.startswith(full_path_working_dir):
        return f'Error: Cannot list "{full_path}" as it is outside the permitted working directory'

    if os.path.isdir(full_path):
        return f'Error: "{full_path}" is a directory, not a file'

    try:
        with open(full_path, "r") as f:
            content = f.read()

        if len(content) > MAX_CHARS_FROM_FILE:
            content = content[:MAX_CHARS_FROM_FILE]
            content += MAX_CHARS_ERROR_MSG_TEMPLATE.format(
                file_path=file_path, max_chars=MAX_CHARS_FROM_FILE
            )

        return content

    except Exception as e:
        return f"Error: {repr(e)}"
