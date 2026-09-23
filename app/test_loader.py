from pathlib import Path
from repository_loader import load_repo
import pprint as pp
print(Path.cwd())
# files= find_python_files("../repositories/sample_repo")

# for file in files:
#     print(file)

# content = read_file("../repositories/sample_repo/main.py")
# print(content)
repo = load_repo("repositories/sample_repo")
pp.pprint(repo)