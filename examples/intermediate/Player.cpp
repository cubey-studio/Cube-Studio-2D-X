#include "Player.h"

Player* Player::create()
{
    auto player = new Player();
    if (player && player->init())
        return player;

    delete player;
    return nullptr;
}

bool Player::init()
{
    if (!Sprite::initWithFile("assets/player.png"))
        return false;

    speed = 200.0f;
    return true;
}

void Player::update(float dt)
{
    CS::Vec2 pos = getPosition();

    if (CS::Input::isKeyPressed(CS::KeyCode::Left))
        pos.x -= speed * dt;
    if (CS::Input::isKeyPressed(CS::KeyCode::Right))
        pos.x += speed * dt;

    setPosition(pos);

    if (CS::Input::isKeyPressed(CS::KeyCode::Space))
        CS::Audio::play("assets/click.wav");
}
