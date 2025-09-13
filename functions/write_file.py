import os


def write_file(working_directory, file_path, content): 
    abs_working_dir = os.path.abspath(working_directory)
    abs_direcotry  = os.path.abspath(os.path.join(working_directory,  file_path))



    if not abs_direcotry.startswith(abs_working_dir): 
        return f"Errors: {abs_file_path} is not a directory"

    if not os.path.isfile(abs_direcotry): 
        parent_dir = os.path.dirname(abs_direcotry) 

        try: 
           os.makedirs(parent_dir) 
        except Exception as e: 
           return f"could not found dir with the {abs_direcotry}, {e}"

    try: 
        with open(abs_direcotry, "r") as f: 
            f.write(content)
            return f"Successfully write content to {abs_direcotry}"

    except Exception as e:
        return f"could not write contnet to file path {abs_direcotry}, {e}"






