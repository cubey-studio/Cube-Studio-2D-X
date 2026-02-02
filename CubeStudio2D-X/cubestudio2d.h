#pragma once
/*
This is the header made/updated in 01/01/2026 that needs to be if type: '#include <CubeStudio2D-X/cubestudio2d.h>'
but, if you have Visual Studio 2026, great but if you have VSCode, don't use it.
Anyways, see the license in https://github.com/cubey-studio/Cube-Studio-2D-X/blob/main/LICENSE
and there is the steps that need to have:
1. Python 3.10 <= 3.14.2 (or later),
2. CMake 4.x.x <= 4.2.2 (or later) &
3. Visual Studio 2026
*/
#ifndef __CUBESTUDIO2DX__
#define __CUBESTUDIO2DX__

#include <string>
#include <vector>
#include <iostream>
#include <memory>
#include <cmath>
#include <map>

#define CUBESTUDIO2DX_VERSION_MAJOR 1
#define CUBESTUDIO2DX_VERSION_MINOR 0
#define CUBESTUDIO2DX_VERSION_PATCH 0

// ------------------------
// NAMESPACE
// ------------------------
#define NS_CS_BEGIN namespace CS {
#define NS_CS_END }

NS_CS_BEGIN

inline void printVersion() {
    std::cout << "Cube Studio 2D-X v" 
              << CUBESTUDIO2DX_VERSION_MAJOR << "." 
              << CUBESTUDIO2DX_VERSION_MINOR << "." 
              << CUBESTUDIO2DX_VERSION_PATCH << std::endl;
}

// ------------------------
// VECTOR 2
// ------------------------
struct Vec2 {
    float x, y;
    Vec2(float xx=0, float yy=0) : x(xx), y(yy) {}
    Vec2 operator+(const Vec2& other) const { return Vec2(x+other.x, y+other.y); }
    Vec2 operator-(const Vec2& other) const { return Vec2(x-other.x, y-other.y); }
    Vec2 operator*(float f) const { return Vec2(x*f, y*f); }
};

// ------------------------
// LABEL
// ------------------------
class Label {
public:
    Label(const std::string& text="") : text(text) {}
    void setText(const std::string& t) { text = t; }
    std::string getText() const { return text; }
    void draw() { std::cout << "[Label] " << text << std::endl; }

private:
    std::string text;
};

// ------------------------
// SPRITE
// ------------------------
class Sprite {
public:
    Sprite(const std::string& filename="") : filename(filename), position(0,0) {}
    void setPosition(const Vec2& pos) { position = pos; }
    Vec2 getPosition() const { return position; }
    void draw() { std::cout << "[Sprite] " << filename << " at (" << position.x << "," << position.y << ")" << std::endl; }

private:
    std::string filename;
    Vec2 position;
};

// ------------------------
// SCENE BASE
// ------------------------
class Scene {
public:
    virtual ~Scene() {}
    virtual void createScene(const std::string& name) {}
    void addLabel(std::shared_ptr<Label> label) { labels.push_back(label); }
    void addSprite(std::shared_ptr<Sprite> sprite) { sprites.push_back(sprite); }

    void draw() {
        for(auto& l : labels) l->draw();
        for(auto& s : sprites) s->draw();
    }

private:
    std::vector<std::shared_ptr<Label>> labels;
    std::vector<std::shared_ptr<Sprite>> sprites;
};

// ------------------------
// ENGINE
// ------------------------
inline void initialize() { std::cout << "Cube Studio 2D-X initializing..." << std::endl; }
inline void shutdown() { std::cout << "Cube Studio 2D-X shutting down..." << std::endl; }
inline void runWithScene(Scene* scene) {
    std::cout << "Running scene..." << std::endl;
    scene->draw();
}

NS_CS_END

#endif // __CUBESTUDIO2DX__
