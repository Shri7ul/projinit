import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s"
)

while True:
    project_name = input("Enter your project name: ").strip()
    if project_name:
        break
    logging.info("Project name cannot be empty. Please try again.")

logging.info(f"Creating project structure for: {project_name}")

files = [
    f"src/{project_name}/__init__.py",

    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/test_unit.py",
    "tests/integration/__init__.py",
    "tests/integration/test_int.py",

    ".github/workflows/ci.yml",

    "requirements.txt",
    "requirements_dev.txt",
    "pyproject.toml",
    "tox.ini",
    "README.md",
    ".gitignore",
]

for file_path in files:
    file_path = Path(file_path)
    dir_path = file_path.parent

    if not dir_path.exists():
        os.makedirs(dir_path, exist_ok=True)
        logging.info(f"Created directory: {dir_path}")

    if not file_path.exists():
        file_path.touch()
        logging.info(f"Created file: {file_path}")

logging.info("Project skeleton created successfully.")
