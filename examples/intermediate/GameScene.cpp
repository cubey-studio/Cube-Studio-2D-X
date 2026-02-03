#include "GameScene.h"

GameScene* GameScene::create()
{
    auto scene = new GameScene();
    if (scene && scene->init())
        return scene;

    delete scene;
    return nullptr;
}

bool GameScene::init()
{
    if (!Scene::init())
        return false;

    player = Player::create();
    player->setPosition(CS::Vec2(480, 270));
    addChild(player);

    info = CS::Label::create("Use arrow keys to move", "Arial", 20);
    info->setPosition(CS::Vec2(480, 500));
    addChild(info);

    scheduleUpdate();
    return true;
}

void GameScene::update(float dt)
{
    player->update(dt);
}