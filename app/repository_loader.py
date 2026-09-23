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

        # the any() checks if  at least ONE thing in this collection True?, if yes it returns TRUE.
        # uncompressed loop: (down)
        # for part in file.parts:
        #     if part in IGNORED_DIRS:
        #         ...
        if any(part in IGNORED_DIRS for part in file.parts):
            continue

        files.append(file)
    return files


def read_file(file_path):
    file_path = Path(file_path)
    # error handling if any files comes thats not utf=8 or cant open
    try:
        with open(file_path, "r" , encoding="utf-8") as file:
            return file.read()
    except (UnicodeDecodeError,OSError):
        return None


def load_repo(repo_path):
    repo_path = Path(repo_path)
    files=find_python_files(repo_path)
    repository = []
    for file in files:
        content = read_file(file)

        if content is None:
            content
        
        repository.append({
            "path": str(file),
            "content": content
            })
    
    return repository



