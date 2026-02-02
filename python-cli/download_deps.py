import sys
import os
import platform

# ===============================
# CONFIG
# ===============================

REQUIRED_PYTHON_MIN = (3, 10)
REQUIRED_PYTHON_MAX = (3, 14, 2)

DEPS_FOLDER = "deps"

DEPENDENCIES = {
    "SDL2": "Core window, input and events",
    "SDL2_image": "Image loading (PNG, JPG)",
    "SDL2_mixer": "Audio playback",
    "SDL2_ttf": "TrueType font rendering",
    "Box2D": "2D physics engine",
    "FreeType": "Font rasterization",
    "GLEW": "OpenGL extensions",
    "OpenAL": "3D audio",
    "libpng": "PNG support",
    "zlib": "Compression",
    "libogg": "Audio container",
    "libvorbis": "Audio codec",
    "rapidjson": "JSON parsing",
    "glm": "Math (vectors, matrices)",
}

# ===============================
# PYTHON VERSION CHECK
# ===============================

def check_python_version():
    version = sys.version_info
    current = (version.major, version.minor)

    if current < REQUIRED_PYTHON_MIN:
        print(
            f"The required version of Python is 3.10 <= 3.14.2 "
            f"but you are using {version.major}.{version.minor} "
            "and it's not required. Please install the version 3.10 or later."
        )
        sys.exit(1)

    if version.major == 3 and version.minor > 14:
        print(
            f"The required version of Python is 3.10 <= 3.14.2 "
            f"but you are using {version.major}.{version.minor}. "
            "This version is not supported yet."
        )
        sys.exit(1)

# ===============================
# UTILS
# ===============================

def log(msg):
    print(f"[cubey] {msg}")

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        log(f"Created folder: {path}")
    else:
        log(f"Folder already exists: {path}")

# ===============================
# DEPENDENCY SETUP
# ===============================

def setup_dependency(name, description):
    dep_path = os.path.join(DEPS_FOLDER, name)

    create_folder(dep_path)
    create_folder(os.path.join(dep_path, "include"))
    create_folder(os.path.join(dep_path, "lib"))
    create_folder(os.path.join(dep_path, "bin"))

    info_file = os.path.join(dep_path, "README.txt")
    if not os.path.exists(info_file):
        with open(info_file, "w", encoding="utf-8") as f:
            f.write(f"{name}\n")
            f.write(f"{description}\n")
            f.write("Downloaded by Cubey CLI\n")

# ===============================
# MAIN DOWNLOAD FUNCTION
# ===============================

def download_dependencies():
    log("Cube Studio 2D-X dependency installer")
    log(f"Platform: {platform.system()} {platform.machine()}")
    log(f"Python: {platform.python_version()}")

    create_folder(DEPS_FOLDER)

    for dep, desc in DEPENDENCIES.items():
        log(f"Setting up dependency: {dep}")
        setup_dependency(dep, desc)

    log("All dependencies are ready.")
    log("You can now build Cube Studio 2D-X using CMake.")

# ===============================
# ENTRY POINT
# ===============================

if __name__ == "__main__":
    check_python_version()
    download_dependencies()