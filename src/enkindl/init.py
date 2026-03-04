from pathlib import Path


PYPROJECT_TEMPLATE = """\
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "{name}"
version = "0.1.0"
description = "{description}"
readme = "README.md"
requires-python = ">=3.12"
license = "MIT"
authors = [
    {{ name = "{author}" }},
]

[project.scripts]
{name} = "{name}.cli:main"
"""

GITIGNORE_TEMPLATE = """\
__pycache__/
*.egg-info/
dist/
build/
.venv/
"""

CLI_TEMPLATE = """\
def main():
    print("{name} is alive!")
"""

README_TEMPLATE = """\
# {name}

{description}
"""


def ask(prompt: str, default: str = "") -> str:
    if default:
        value = input(f"{prompt} [{default}]: ").strip()
        return value if value else default
    return input(f"{prompt}: ").strip()


def scaffold(name: str) -> None:
    root = Path(name)

    if root.exists():
        print(f"Error: folder '{name}' already exists.")
        raise SystemExit(1)

    print(f"Setting up '{name}'...\n")

    description = ask("Short description", "A Python project")
    author = ask("Author name", "")

    # Create folder structure
    src = root / "src" / name
    src.mkdir(parents=True)

    # Write files
    (root / "pyproject.toml").write_text(
        PYPROJECT_TEMPLATE.format(
            name=name,
            description=description,
            author=author,
        )
    )
    (root / ".gitignore").write_text(GITIGNORE_TEMPLATE)
    (root / "README.md").write_text(
        README_TEMPLATE.format(name=name, description=description)
    )
    (src / "__init__.py").write_text("")
    (src / "cli.py").write_text(CLI_TEMPLATE.format(name=name))

    print(f"\nCreated project '{name}/'")
    print()
    print("Next steps:")
    print(f"  cd {name}")
    print(f"  python -m venv .venv")
    print(f"  pip install -e .")
    print(f"  {name}")