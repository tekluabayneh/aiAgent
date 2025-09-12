from functions.get_files_info import get_files_info

def main(): 
    working_dir = "calculator" 
    root_contents = get_files_info(working_dir) 
    pkg_content = get_files_info(working_dir, "pkg")
    pkg_content = get_files_info(working_dir, "/bin")
    pkg_content = get_files_info(working_dir, "../")
    print(root_contents)
    print(pkg_content)




main()
