#include <CubeStudio2D-X/cubestudio2d.h>
#include "GameScene.h"

int main(int argc, char** argv)
{
    CS::Application app;

    app.setWindowTitle("Cube Studio 2D-X - Basic Example");
    app.setWindowSize(800, 600);

    app.run(GameScene::create());

    return 0;
}