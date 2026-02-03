#pragma once
#include <CubeStudio2D-X/cubestudio2d.h>

class Player : public CS::Sprite
{
public:
    static Player* create();

    virtual bool init();
    void update(float dt);

private:
    float speed;
};