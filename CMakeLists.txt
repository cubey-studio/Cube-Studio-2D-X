cmake_minimum_required(VERSION 3.16)
project(CubeStudio2D-X LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Engine library
add_library(CubeStudio2DX STATIC cubestudio2d.cpp cubestudio2d.h)

target_include_directories(CubeStudio2DX PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

# Subdirectories
add_subdirectory(examples/basic)