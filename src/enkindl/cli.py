
import argparse 

from enkindl.init import scaffold

def main():
    parser = argparse.ArgumentParser(
        prog="enkindl",
        description="A tiny CLI tool that scaffolds Python projects for beginners."
    )

    subparsers = parser.add_subparsers(dest="command")

    # enkindl init <project_name>
    init_parser = subparsers.add_parser("init", help="Scaffold a new Python project")
    init_parser.add_argument("name", help="Name of the project to create")

    # enkindl explain <topic>
    explain_parser = subparsers.add_parser("explain", help="Explain a Python concept")
    explain_parser.add_argument("topic", help="Topic to explain")

    args = parser.parse_args()

    if args.command == "init":
        scaffold(args.name)
    elif args.command == "explain":
        print(f"Explaining: {args.topic}")
    else:
        parser.print_help()