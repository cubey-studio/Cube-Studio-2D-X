#include <CubeStudio2D-X/cubestudio2d.h>

NS_CS_BEGIN

inline void initAudio() {
    std::cout << "Audio system initialized" << std::endl;
}

inline void initPhysics() {
    std::cout << "Physics engine initialized" << std::endl;
}

void initialize() {
    std::cout << "Cube Studio 2D-X Engine v" 
              << CUBESTUDIO2DX_VERSION_MAJOR << "." 
              << CUBESTUDIO2DX_VERSION_MINOR << "." 
              << CUBESTUDIO2DX_VERSION_PATCH 
              << " starting..." << std::endl;
    initAudio();
    initPhysics();
}

void shutdown() {
    std::cout << "Cube Studio 2D-X Engine shutting down..." << std::endl;
}

void runWithScene(Scene* scene) {
    if(!scene) {
        std::cout << "❌ No scene to run!" << std::endl;
        return;
    }
    std::cout << "Running scene..." << std::endl;
    scene->draw();
}

NS_CS_END