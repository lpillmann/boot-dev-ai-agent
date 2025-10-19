import os
import subprocess


def run_python_file(working_directory: str, file_path: str, args: list[str] = []):
    full_path_working_dir = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not full_path.startswith(full_path_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'

    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        completed_process = subprocess.run(
            ["uv", "run", "python", full_path] + args,
            timeout=30,
            capture_output=True,
            check=True,
            text=True,
        )
        returncode = completed_process.returncode
        stdout = f"STDOUT:\n{completed_process.stdout}"
        stderr = f"STDERR:\n{completed_process.stderr}"
        extra = f"Process exited with code {returncode}" if returncode != 0 else ""

        if not stdout and not stderr:
            return "No output produced."

        return f"{stdout}\n{stderr}\n{extra}"

    except Exception as e:
        return f"Error: executing Python file: {e}"
