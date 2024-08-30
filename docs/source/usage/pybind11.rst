Python Bindings for C++
=======================

This repository demonstrates how to use pybind11 to build Python modules out of
C++ code so it can be used in Python like a "normal" Python module.

You can see our example `libs/src_cxx/ <https://github.com/yoctoyotta1024/GoodSciProjTemplate/blob/main/libs/src_cxx/mock_cxx.hpp>`_.
To make the Python bindings you can simply perform

.. code-block:: console

  $ cmake -S ./ -B ./build
  $ cd build && make

which fetches and uses pybind11 (see CMakeLists.txt) to make a Python module out of the C++ code.


Deleting C++ From This Repository
#################################

Not using C++? Don't want any bindings? Then you can remove certain files and doxygen from you repository.


Pybind11
########
https://github.com/pybind/pybind11/
