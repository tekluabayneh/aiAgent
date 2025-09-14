
import os 
import subprocess

def run_python_file(working_directory:str, file_path:str): 
    abs_working_dir = os.path.abspath(working_directory)
    abs_direcotry = os.path.abspath(os.path.join(working_directory,  file_path))

    if not abs_direcotry.startswith(abs_working_dir): 
        return f"Errors: {abs_working_dir} is not a directory"


    if not os.path.isfile(abs_direcotry): 
        return f"Errors: {abs_direcotry} is not a file directory"

    if not file_path.endswith(".py"): 
        return f"Errors: {abs_direcotry} is not a python file"



    try: 
        output = subprocess.run(["python", file_path], cmd=abs_working_dir, timeout=30)

        final_string = f"""
           STDOUT: {output.stdout}
           STDIN: {output.stderr}
           """

        if final_string.stdout == "" and output.stdrr == "": 
            final_string = "No output produced."

        if final_string.returnCode != 0: 
            final_string += f"process exited with code {output.returnCode}"
    except Exception as e:
        return f"cound not run python file"








