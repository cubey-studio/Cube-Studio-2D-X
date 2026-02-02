#pragma once

#include <CubeStudio2D-X/cubestudio2d.h>

class GameScene : public CS::Scene
{
public:
    static GameScene* create();

    virtual bool init() override;
    virtual void update(float dt) override;

private:
    CS::Sprite* logo;
    CS::Label* title;
};