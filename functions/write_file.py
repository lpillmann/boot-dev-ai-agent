import os

from google.genai import types


def write_file(working_directory: str, file_path: str, content: str):
    full_path_working_dir = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not full_path.startswith(full_path_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(full_path):
        dir_name = os.path.dirname(full_path)
        os.makedirs(dir_name, exist_ok=True)

    try:
        with open(full_path, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: {repr(e)}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file, contrained to be located within working directory. If the file doesn't exist, the function creates it. Overwrites existing content.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to be written to.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Text content to be written to the file",
            ),
        },
    ),
)
