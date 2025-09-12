MAX_CHARS = 1000

def get_file_content(working_directory, file_path): 
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(working_dir)
    abs_direcotry  = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_direcotry.startswith(abs_working_dir): 
        return f"Errors: {abs_file_path} is not a directory"

    if not os.path.isfile(abs_file_path): 
        return f"Errors: {file_path} is not a file"

    get_file_content = "" 
    with open(abs_file_path, "r") as f: 
        get_file_content = f.read(MAX_CHARS)



