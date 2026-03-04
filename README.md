# enkindl

A tiny CLI tool that scaffolds Python projects for beginners.

No frameworks. No magic. Just the right files in the right places, with plain-English explanations of what everything does.

## Install

```
pip install enkindl
```

## Usage

### Scaffold a new project

```
enkindl init myproject
```

This creates a ready-to-go Python project:

```
myproject/
├── src/
│   └── myproject/
│       ├── __init__.py
│       └── cli.py
├── tests/
│   └── test_cli.py
├── pyproject.toml
├── README.md
└── .gitignore
```

You'll be prompted for a description and author name. The generated project is immediately installable:

```
cd myproject
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
myproject                   # your CLI command works!
```

It even comes with a passing test:

```
pip install pytest
pytest
```

### Explain Python concepts

New to Python packaging? Ask enkindl:

```
enkindl explain pyproject.toml
enkindl explain __init__.py
enkindl explain venv
enkindl explain src-layout
enkindl explain pip-install-e
enkindl explain requirements.txt
enkindl explain .gitignore
enkindl explain build
enkindl explain pypi
enkindl explain entry-points
enkindl explain pytest
```

Don't know what's available? Just ask for a topic that doesn't exist and enkindl will list them all.

## Why?

Starting a Python project shouldn't require reading five blog posts and three Stack Overflow threads. enkindl gives you the modern, recommended project structure in one command, and explains every piece of it.

## Built with

- Python 3.12+
- Standard library only (argparse, pathlib)
- Zero dependencies

## License

MIT