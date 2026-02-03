#include "GameApp.h"
#include "GameScene.h"

bool GameApp::onInit()
{
    setWindowTitle("Cube Studio 2D-X - Intermediate Example");
    setWindowSize(960, 540);

    runWithScene(GameScene::create());
    return true;
}