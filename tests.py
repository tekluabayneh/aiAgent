from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file 
from functions.run_python import run_python_file 

def main(): 
    working_dir = "calculator" 
    # root_contents = get_files_info(working_dir) 
    # pkg_content = get_files_info(working_dir, "pkg")
    # pkg_content = get_files_info(working_dir, "/bin")
    # pkg_content = get_files_info(working_dir, "../")
    # print(root_contents)
    # print(pkg_content)
    #

    # print(get_file_content(working_dir, "lorem.txt"))
    # print(write_file(working_dir, "morelorem.txt", "this is the file man"))


    print(run_python_file(working_dir, "main.py"))


main()
