
import ast

def nunu(a,b):
    c=a+b
    return c
tree = ast.parse("from pathlib import Path\n\nIGNORED_DIRS= {\n    \".git\",\n    \".venv\",\n    \"__pycache__\",\n    \"node_modules\",\n}\n\ndef find_python_files(repo_path):\n    repo_path = Path(repo_path)\n\n    files = []\n\n    for file in repo_path.rglob(\"*.py\"):\n        relative_path = file.relative_to(repo_path)\n        if any(part in IGNORED_DIRS for part in relative_path.parts):\n            continue\n\n        files.append(file)\n    return sorted(files)\n\n\ndef read_file(file_path):\n    file_path = Path(file_path)\n    try:\n        with open(file_path, \"r\" , encoding=\"utf-8\") as file:\n            return file.read()\n    except (UnicodeDecodeError,OSError):\n        return None\n\n\ndef load_repo(repo_path):\n    repo_path = Path(repo_path)\n    if not repo_path.is_dir():\n        raise NotADirectoryError(\n            f\"Repository directory not found: {repo_path}\"\n        )\n    files=find_python_files(repo_path)\n\n    \n    repository = []\n    for file in files:\n        content = read_file(file)\n\n        if content is None:\n            continue\n        if not content.strip():\n            continue\n        \n        repository.append({\n            \"path\": str(file.relative_to(repo_path)),\n            \"content\": content\n            })\n    \n    return repository"
)

print(tree)