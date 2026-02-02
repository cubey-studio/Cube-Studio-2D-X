cmake_minimum_required(VERSION 3.16)
project(BasicExample LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)

add_executable(basic_example main.cpp game.cpp game.h)

# Linkar com engine
target_link_libraries(basic_example CubeStudio2DX)
target_include_directories(basic_example PUBLIC ../../)