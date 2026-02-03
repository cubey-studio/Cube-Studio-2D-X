#pragma once
#include <CubeStudio2D-X/cubestudio2d.h>
#include "Player.h"

class GameScene : public CS::Scene
{
public:
    static GameScene* create();

    virtual bool init() override;
    virtual void update(float dt) override;

private:
    Player* player;
    CS::Label* info;
};