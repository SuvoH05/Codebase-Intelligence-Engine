from pathlib import Path

def find_python_files(repo_path):
    repo_path = Path(repo_path)
    return list(repo_path.rglob("*.py"))

def read_file(file_path):
    file_path = Path(file_path)

    with open(file_path, "r" , encoding="utf-8") as file:
        return file.read()

def load_repo(repo_path):
    repo_path = Path(repo_path)
    files=find_python_files()
    repository = []
    for file in files:
        repository.append(file)

