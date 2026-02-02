import sys
import os
from download_deps import download_dependencies

# Engine version
CUBE_STUDIO_VERSION = "1.0.0"

def show_version():
    print(f"Cube Studio 2D-X version {CUBE_STUDIO_VERSION}")

def create_project(args):
    if "--project" in args and "--path" in args:
        project_name = args[args.index("--project") + 1]
        project_path = args[args.index("--path") + 1]
        print(f"Creating new C++ project '{project_name}' at '{project_path}'")
        # Aqui você pode gerar a estrutura de pastas e arquivos do projeto
    else:
        print("Error: You must specify --project and --path")

def define_folder(args):
    if "-folder" in args:
        folder = args[args.index("-folder") + 1]
        print(f"Folder defined: {folder}")

def run_project(args):
    if len(args) == 0:
        print("Running current project...")
    else:
        path = args[0]
        print(f"Running project at: {path}")

def download_deps(args):
    print("Downloading engine dependencies...")
    download_dependencies()
    print("Dependencies downloaded into 'deps/' folder.")

def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print("Cubey CLI - use --help for commands")
        return

    if "--version" in args:
        show_version()
    elif "new" in args:
        create_project(args)
    elif "--define" in args:
        define_folder(args)
    elif "--run" in args:
        run_project(args)
    elif "--download" in args and "-deps" in args:
        download_deps(args)
    else:
        print("Unknown command. Use --help for available commands.")

if __name__ == "__main__":
    main()