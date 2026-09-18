from repository_loader import find_python_files,read_file

files= find_python_files("../repositories/sample_repo")

for file in files:
    print(file)

content = read_file("../repositories/sample_repo/main.py")
print(content)
