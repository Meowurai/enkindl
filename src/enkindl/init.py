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

TEST_TEMPLATE = """\
from {name}.cli import main


def test_main(capsys):
    main()
    output = capsys.readouterr().out
    assert "{name} is alive!" in output
"""


def ask(prompt: str, default: str = "") -> str:
    """
    Prompt the user for input with an optional default value.
    
    Args:
        prompt (str): The message to display to the user.
        default (str, optional): The default value to return if the user provides no input. Defaults to "".
    
    Returns:
        str: The user's input, stripped of leading/trailing whitespace, or the default value if no input was provided.
    """
    if default:
        value = input(f"{prompt} [{default}]: ").strip()
        return value if value else default
    return input(f"{prompt}: ").strip()


def scaffold(name: str) -> None:
    """
    Create a new Python project structure with scaffolding files.

    This function sets up a basic Python project layout including:
    - A source directory structure (src/{name})
    - Configuration files (pyproject.toml, .gitignore, README.md)
    - An __init__.py file for the package
    - A CLI module template
    - A test directory with a sample test file

    Args:
        name (str): The name of the project to scaffold.

    Raises:
        SystemExit: If a folder with the given name already exists.

    Example:
        >>> scaffold("my_project")
        Setting up 'my_project'...
        Short description: My awesome Python project
        Author name: John Doe
        Created project 'my_project/'
        ...
    """
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

    # Create tests
    tests = root / "tests"
    tests.mkdir()
    (tests / f"test_cli.py").write_text(TEST_TEMPLATE.format(name=name))

    print(f"\nCreated project '{name}/'")
    print()
    print("Next steps:")
    print(f"  cd {name}")
    print(f"  python3 -m venv .venv")
    print(f"  source .venv/bin/activate   # Windows: .venv\\Scripts\\activate")
    print(f"  pip install -e .")
    print(f"  {name}")
    print()
    print("Run tests:")
    print(f"  pip install pytest")
    print(f"  pytest")