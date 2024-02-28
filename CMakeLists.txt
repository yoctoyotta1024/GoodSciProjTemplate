cmake_minimum_required(VERSION 3.18.0)
project(project
  LANGUAGES CXX
  DESCRIPTION "GoodSciProjTemplate"
  VERSION 0.0.0
)

## Use the pybind11 package from .gitmodules
add_subdirectory(external/pybind11)

## Create the Python extension module from C++ source files
set(SOURCES libs/src_cxx/mock.cpp)
pybind11_add_module(mock_cxx MODULE ${SOURCES})

set_target_properties(mock_cxx PROPERTIES
  CXX_STANDARD 20
  CMAKE_CXX_STANDARD_REQUIRED ON
  CMAKE_CXX_EXTENSIONS ON)