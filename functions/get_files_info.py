import os
def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path(directory)
    if directory ==".": 
        abs_direcotry  = os.path.abspath(directory)

    if not abs_direcotry.startswith(abs_working_dir): 
        return f"Errors: {directory} is not a directory"


    final_response = ""
    contents = os.listdir(abs_direcotry)
    for conent in contents: 
        content_path = os.path(abs_direcotry, conent)
        size = os.path.get_size(content_path)



