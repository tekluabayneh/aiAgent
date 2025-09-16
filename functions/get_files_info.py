import os
from google.genai import types 

def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)

    # Determine target directory
    if directory is None: 
        abs_directory = abs_working_dir
    else: 
        abs_directory = os.path.abspath(os.path.join(working_directory, directory))

    # Ensure directory is inside working directory
    if not abs_directory.startswith(abs_working_dir): 
        return f"Error: {directory} is outside the working directory"

    try:
        contents = os.listdir(abs_directory)
    except Exception as e:
        return f"Error listing directory {abs_directory}: {e}"

    final_response = ""
    for content in contents: 
        content_path = os.path.join(abs_directory, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        final_response += f"{content}: size={size} bytes, is_dir={is_dir}\n"

    return final_response


# Updated schema
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes and type, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base directory to list files from."
            ),
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Optional subdirectory relative to the working directory. If not provided, lists files in the working directory itself."
            ),
        },
        required=["working_directory"],
    ),
)

