import os
import subprocess
from google.genai import types 

def run_python_file(working_directory: str, file_path: str, args =[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_directory.startswith(abs_working_dir):
        return f"Errors: {abs_working_dir} is not a directory"

    if not os.path.isfile(abs_directory):
        return f"Errors: {abs_directory} is not a file directory"

    if not file_path.endswith(".py"):
        return f"Errors: {abs_directory} is not a python file"

    try:
        final_args = ["python", file_path]
        final_args.extend(args)

        output = subprocess.run(
            final_args,
            cwd=abs_working_dir,
            timeout=30,
            capture_output=True,
            text=True
        )

        if output.stdout == "" and output.stderr == "":
            return "No output produced."

        final_string = f"""
        STDOUT: {output.stdout}
        STDERR: {output.stderr}
        """

        if output.returncode != 0:
            final_string += f"\nProcess exited with code {output.returncode}"

        return final_string

    except Exception as e:
        return f"Could not run python file: {e}"

schema_run_file_content = types.FunctionDeclaration(
    name="run_python_file",
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



