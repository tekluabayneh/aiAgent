import os
import subprocess
from google.genai import types 

def run_python_file(working_directory: str, file_path: str, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: {file_path} is outside the working directory"

    if not os.path.isfile(abs_file_path):
        return f"Error: {file_path} does not exist or is not a file"

    if not file_path.endswith(".py"):
        return f"Error: {file_path} is not a Python file"

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

        if not output.stdout and not output.stderr:
            return "No output produced."

        final_string = f"STDOUT:\n{output.stdout}\nSTDERR:\n{output.stderr}"
        if output.returncode != 0:
            final_string += f"\nProcess exited with code {output.returncode}"

        return final_string

    except Exception as e:
        return f"Could not run python file: {e}"


# Updated schema to match function arguments
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python file within the specified working directory with optional arguments and returns stdout and stderr.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base directory where the Python file is located."
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path to the Python file within the working directory."
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional arguments to pass to the Python file."
            ),
        },
        required=["working_directory", "file_path"],
    ),
)

