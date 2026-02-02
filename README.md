# Cube Studio 2D-X v1.0
Cube Studio 2D-X is a 2D C++ game engine, inspired by Cocos2d-x, designed to be modular, lightweight, and cross-platform.
It provides the core functionality to create 2D games, including scenes, labels, sprites, vector math, audio, and physics support.
## Features
`Scenes`: Create and manage multiple scenes for your game.
`Labels`: Display text on the screen.
`Sprites`: Render images with position and basic manipulation.
`Vec2`: 2D vector math for positions, movements, and calculations.
`Audio` & `Physics stubs`: Prepare your game for audio and physics integration.
`Engine Lifecycle`: `initialize()`, `shutdown()`, `runWithScene()`.
`CMake Build System`: Build on Windows, macOS, and Linux.
`CLI cubey`: Create new projects, run builds, and download dependencies.
`Dependencies`: SDL2, SDL2_mixer, GLEW, FreeType, Box2D, libpng, libvorbis, zlib, rapidjson.
### Project Structure
```
CubeStudio2D-X/
CMakeLists.txt         - Build configuration for the engine
cubestudio2d.h         - Main header file
cubestudio2d.cpp       - Engine implementation
deps/                  - External libraries
examples/              - Example projects
basic/
main.cpp
game.h
game.cpp
python-cli/            - CLI for creating projects
setup.py             - Main CLI entry point
download_deps.py     - Downloads all dependencies automatically
README.md              - This documentation
```

#### Installation
Clone the repository:
```Bash
git clone https://github.com/Cubey-Studio/CubeStudio2D-X.git
cd CubeStudio2D-X
```

Install Python dependencies
Requires Python 3.10 ≤ version ≤ 3.14.2
```Bash
pip install .
```
Download external dependencies
```Bash
cubey setup-deps
```
Downloads SDL2, SDL2_mixer, GLEW, FreeType, Box2D, libpng, libvorbis, zlib, rapidjson, and extracts them into deps/.
Using the CLI
Create a new project:
```Bash
cubey new --project mygame --path com.example.mygame -cpp
```
Define active folder (optional):
```Bash
cubey --define -folder "C:\Path\To\MyGame"
```
Build and run project:
```Bash
cubey --run
```
Example: Basic C++ Project
main.cpp:
```Cpp
#include <CubeStudio2D-X/cubestudio2d.h>
#include "game.h"
using namespace CS;
int main() {
    CS::initialize();
    GameScene* scene = new GameScene();
    scene->createScene("Level 1");
    CS::runWithScene(scene);
    CS::shutdown();
    delete scene;
    return 0;
}
```
game.h & game.cpp
Example of creating a scene, adding labels and sprites using the engine.
Build with CMake:
```Bash
mkdir build
cd build
cmake ..
cmake --build .
```
Windows: Use Visual Studio 2026 recommended
Linux / macOS: Use GCC / Clang with CMake
Contributing
Open an issue or pull request
Follow the coding style: NS_CS_BEGIN / NS_CS_END for namespaces
All new features should be compatible with Python CLI and CMake builds
License
Cube Studio 2D-X v1.0 is MIT Licensed. See LICENSE file for details.
Notes
This is a v1.0 minimal engine, designed to be expanded.
Audio, physics, and graphics are stubbed but ready for real libraries.
Compatible with Windows CMD / PowerShell.
Can be used as a framework for new C++ 2D games.