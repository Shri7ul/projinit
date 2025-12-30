import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s"
)

logging.info("Creating projinit base template files...")

BASE_PATH = Path("projinit/templates/base")

FILES = [
    # CI
    "ci.yml.txt",

    # Core configs
    "pyproject.toml.txt",
    "tox.ini.txt",
    "README.md.txt",

    # Requirements
    "requirements.txt.txt",
    "requirements_dev.txt.txt",

    # Tests
    "tests/unit/test_unit.py.txt",
    "tests/integration/test_int.py.txt",

    # Git ignore
    ".gitignore.txt",
]

for file in FILES:
    file_path = BASE_PATH / file
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        file_path.touch()
        logging.info(f"Created template file: {file_path}")
    else:
        logging.info(f"Template already exists: {file_path}")

logging.info("✅ Base template structure ready.")
