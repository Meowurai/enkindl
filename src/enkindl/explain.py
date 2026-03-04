

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
"requirements.txt": """
requirements.txt is a simple list of packages your project depends on.

Example:
    requests==2.31.0
    pandas>=2.0

Each line is a package name, optionally pinned to a version.

It's used with: pip install -r requirements.txt

For modern projects, you can also list dependencies in pyproject.toml
under [project.dependencies] instead. But requirements.txt is still
widely used, especially for applications (vs. libraries).
""",
    ".gitignore": """
.gitignore tells git which files to NOT track.

Common entries for Python projects:
    __pycache__/    - compiled bytecode (Python creates this automatically)
    *.egg-info/     - package metadata (created during install)
    dist/           - built packages (created when you build for PyPI)
    .venv/          - your virtual environment

Without a .gitignore, you'd accidentally commit thousands of
generated files. Always set this up before your first commit.
""",
    "build": """
"Building" a Python package means turning your source code into
a format that pip can install.

The two formats are:
    sdist   - a source distribution (basically a .tar.gz of your code)
    wheel   - a pre-built distribution (.whl file, installs faster)

You build with: python -m build
This reads your pyproject.toml and creates both formats in dist/.

You don't need to build during development — pip install -e . handles
that. You only build when you're ready to publish to PyPI.
""",
    "pypi": """
PyPI (Python Package Index) is where pip downloads packages from.

When you type: pip install requests
pip goes to pypi.org, finds the 'requests' package, and installs it.

Anyone can publish packages to PyPI. To publish yours:
    1. Build it:    python -m build
    2. Upload it:   python -m twine upload dist/*

There's also TestPyPI (test.pypi.org) for practicing without
polluting the real index.
""",
    "entry-points": """
Entry points are how a Python package creates terminal commands.

In pyproject.toml:
    [project.scripts]
    mycommand = "mypackage.cli:main"

This tells pip: "when you install this package, create a command
called 'mycommand' that runs the main() function in mypackage/cli.py."

That's why after pip install, you can type the command name directly
in your terminal — pip generated a small script that calls your function.
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