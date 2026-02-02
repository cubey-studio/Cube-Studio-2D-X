#include "GameScene.h"

GameScene* GameScene::create()
{
    GameScene* scene = new GameScene();
    if (scene && scene->init())
        return scene;

    delete scene;
    return nullptr;
}

bool GameScene::init()
{
    if (!Scene::init())
        return false;

    // Logo sprite
    logo = CS::Sprite::create("assets/logo.png");
    logo->setPosition(CS::Vec2(400, 300));
    addChild(logo);

    // Title label
    title = CS::Label::create("Hello Cube Studio 2D-X", "Arial", 24);
    title->setPosition(CS::Vec2(400, 500));
    addChild(title);

    scheduleUpdate();
    return true;
}

void GameScene::update(float dt)
{
    // Simple rotation
    float rotation = logo->getRotation();
    logo->setRotation(rotation + 30.0f * dt);
}