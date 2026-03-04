

TOPICS = {
    "pyproject.toml": """
pyproject.toml is your project's ID card.

It tells Python three things:
  1. How to BUILD your project (the [build-system] section)
  2. What your project IS (the [project] section — name, version, etc.)
  3. What commands to create (the [project.scripts] section)

Before pyproject.toml existed, people used setup.py which was messy
and confusing. pyproject.toml replaced it in modern Python.

Every Python project you publish should have one.
""",
    "__init__.py": """
__init__.py is a marker file that tells Python "this folder is a package."

Without it, Python won't let you import code from the folder.
It can be completely empty and still do its job.

You can also put code in it — like a version number:
    __version__ = "0.1.0"

But keeping it empty is totally fine for most projects.
""",
    "venv": """
A virtual environment (venv) is an isolated bubble for your project.

Without it, every pip install goes into your system Python, and
different projects can fight over which version of a library to use.

With a venv, each project gets its own copy of Python and its own
packages. Create one with:
    python -m venv .venv

Activate it:
    Windows:    .venv\\Scripts\\activate
    Mac/Linux:  source .venv/bin/activate

You'll see (.venv) in your prompt when it's active.
""",
    "src-layout": """
The src/ layout means putting your code inside a src/ folder:
    myproject/
        src/
            myproject/
                __init__.py

Why not just put the code directly in the root?

Because of a subtle bug: if your package folder sits next to
pyproject.toml, Python might import the local folder instead of
the installed package. The src/ folder prevents this by keeping
your source code out of the default import path.

It's a best practice recommended by the Python Packaging Authority.
""",
    "pip-install-e": """
pip install -e . installs your project in "editable" mode.

Normal install: pip copies your code into the Python environment.
If you change your code, you have to reinstall.

Editable install: pip creates a link to your source folder.
Changes to your code are immediately available — no reinstall.

The "." means "install the project in the current directory."
The "-e" means "make it editable."

This is the go-to command during development.
""",
}

def explain(topic: str) -> None:
    result = TOPICS.get(topic)

    if result:
        print(result.strip())
    else:
        print(f"Unknown topic: '{topic}'\n")
        print("Available topics:")
        for key in sorted(TOPICS):
            print(f"  - {key}")