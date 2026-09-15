from pathlib import Path

def find_python_files(repo_path):
    repo_path = Path(repo_path)
    return list(repo_path.rglob("*.py"))


