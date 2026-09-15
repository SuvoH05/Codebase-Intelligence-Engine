from repository_loader import find_python_files

files= find_python_files("../repositories/sample_repo")

for file in files:
    print(file)