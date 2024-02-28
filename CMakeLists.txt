cmake_minimum_required(VERSION 3.18.0)
project(project
  LANGUAGES CXX
  DESCRIPTION "GoodSciProjTemplate"
  VERSION 0.0.0
)

## Find and use the pybind11 package
include(FetchContent)
FetchContent_Declare(
  pybind11
  DOWNLOAD_EXTRACT_TIMESTAMP TRUE
  URL https://github.com/pybind/pybind11/archive/refs/tags/v2.11.1.tar.gz
  URL_HASH MD5=49e92f92244021912a56935918c927d0
)
FetchContent_MakeAvailable(pybind11)

## Create the Python extension module from C++ source files
set(SOURCES libs/src_cxx/mock.cpp)
pybind11_add_module(mock_cxx MODULE ${SOURCES})

set_target_properties(mock_cxx PROPERTIES
  CXX_STANDARD 20
  CMAKE_CXX_STANDARD_REQUIRED ON
  CMAKE_CXX_EXTENSIONS ON)