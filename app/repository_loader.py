from pathlib import Path

IGNORED_DIRS= {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
}

def find_python_files(repo_path):
    repo_path = Path(repo_path)

    files = []

    for file in repo_path.rglob("*.py"):
        if any(part in IGNORED_DIRS for part in file.parts):
            continue

        files.append(file)
    return files


def read_file(file_path):
    file_path = Path(file_path)

    with open(file_path, "r" , encoding="utf-8") as file:
        return file.read()

def load_repo(repo_path):
    repo_path = Path(repo_path)
    files=find_python_files(repo_path)
    repository = []
    for file in files:
        content = read_file(file)
        
        repository.append({
            "path": str(file),
            "content": content
            })
    
    return repository



