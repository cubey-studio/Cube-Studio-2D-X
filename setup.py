import sys
import os
import json
import subprocess

MIN_VERSION = (3, 10)
MAX_VERSION = (3, 14, 2)
v = sys.version_info

if v < MIN_VERSION or v > MAX_VERSION:
    print(f"""
❌ The required version of Python is 3.10 <= 3.14.2
but you are using {v.major}.{v.minor}.{v.micro} and it's not required.
Please install Python 3.10 or later.
""")
    sys.exit(1)


CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".cubey")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def set_active_project(path):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump({"active_project": path}, f, indent=4)
    print(f"✔ Active project set:\n{path}")

def get_active_project():
    if not os.path.exists(CONFIG_FILE):
        return None
    with open(CONFIG_FILE, "r") as f:
        return json.load(f).get("active_project")
        
def create_project(args):
    if "--project" not in args or "--path" not in args:
        print("❌ Usage: cubey new --project NAME --path PACKAGE -cpp")
        return

    name = args[args.index("--project") + 1]
    package = args[args.index("--path") + 1]

    os.makedirs(name, exist_ok=True)
    os.makedirs(f"{name}/src", exist_ok=True)
    os.makedirs(f"{name}/assets", exist_ok=True)

    # main.cpp
    main_cpp = f"""#include <CubeStudio2D-X/cubestudio2d.h>

class Game : public CS::Scene {{
public:
    void createScene(std::string scene) override {{}}
}};

int main() {{
    CS::initialize();
    CS::runWithScene(new Game());
    CS::shutdown();
    return 0;
}}
"""
    with open(f"{name}/src/main.cpp", "w") as f:
        f.write(main_cpp)

    # CMakeLists.txt
    cmake = f"""cmake_minimum_required(VERSION 3.16)
project({name} LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)

add_executable({name} src/main.cpp)

target_link_libraries({name} CubeStudio2DX)
target_include_directories({name} PUBLIC ../CubeStudio2D-X)
"""
    with open(f"{name}/CMakeLists.txt", "w") as f:
        f.write(cmake)

    set_active_project(os.path.abspath(name))
    print(f"✔ Project '{name}' created successfully")

def run_project(path=None):
    if path is None:
        path = get_active_project()

    if not path or not os.path.exists(path):
        print("❌ No active project defined. Use --define -folder PATH or 'cubey new ...'")
        return

    build_dir = os.path.join(path, "build")
    os.makedirs(build_dir, exist_ok=True)

    print(f"⬇ Running CMake in {build_dir} ...")
    subprocess.call(["cmake", ".."], cwd=build_dir)
    subprocess.call(["cmake", "--build", "."], cwd=build_dir)
    
    exe_path = None
    for root, _, files in os.walk(build_dir):
        for f in files:
            if f.endswith(".exe"):
                exe_path = os.path.join(root, f)
                break
        if exe_path:
            break

    if exe_path:
        print(f"▶ Running {exe_path}")
        subprocess.call([exe_path])
    else:
        print("❌ Executable not found")

def cubey():
    args = sys.argv[1:]

    if not args:
        print("Cubey CLI - Commands: new, --define -folder, --run")
        return

    # cubey new ...
    if args[0] == "new":
        create_project(args[1:])
        return

    # cubey --define -folder PATH
    if "--define" in args and "-folder" in args:
        folder = args[args.index("-folder") + 1]
        set_active_project(folder)
        return

    # cubey --run [PATH]
    if "--run" in args:
        path = args[-1] if len(args) > 1 else None
        run_project(path)
        return

    print("❌ Unknown command")
    return

# ===============================
# SETUP PIP ENTRY POINT
# ===============================
from setuptools import setup

setup(
    name="cubey",
    version="1.0.0",
    py_modules=["setup"],
    entry_points={
        "console_scripts": [
            "cubey=setup:cubey"
        ]
    },
  )
