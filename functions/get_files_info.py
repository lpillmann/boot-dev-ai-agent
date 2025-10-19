import os


def get_files_info(working_directory: str, directory: str = "."):
    full_path_working_dir = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, directory))

    if not full_path.startswith(full_path_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    contents_list = os.listdir(full_path)
    contents_list_formatted: list[str] = []
    for item in contents_list:
        file_size = os.path.getsize(os.path.join(full_path, item))
        is_dir = os.path.isdir(os.path.join(full_path, item))
        contents_list_formatted.append(
            f" - {item}: file_size={file_size} bytes, is_dir={is_dir}"
        )

    directory_alias = "current" if directory == "." else f"'{directory}'"
    output_template = (
        "Result for {directory_alias} directory: \n{contents_list_formatted}"
    )

    return output_template.format(
        directory_alias=directory_alias,
        contents_list_formatted="\n".join(contents_list_formatted),
    )
