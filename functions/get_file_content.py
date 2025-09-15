import os
from google.genai import types 

MAX_CHARS = 1000

def get_file_content(working_directory, file_path): 
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(file_path)
    abs_direcotry  = os.path.abspath(os.path.join(working_directory,  file_path))
 
    if not abs_direcotry.startswith(abs_working_dir): 
        return f"Errors: {abs_file_path} is not a directory"

    if not os.path.isfile(abs_direcotry): 
        return f"Errors: {file_path} is not a file"


    file_content_setting = "" 

    try:
        with open(abs_direcotry, "r") as f: 
            file_content_setting = f.read(MAX_CHARS)

            if len(file_content_setting) >= MAX_CHARS: 
                file_content_setting += f"...file {file_path}, truncated at 10000 char" 

    except Exception as e:
        return f"Exeption reading file: {e}"


    return file_content_setting


schema_get_file_content= types.FunctionDeclaration(
    name="get_file_content",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)



