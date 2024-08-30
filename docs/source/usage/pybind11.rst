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

Not using C++? Don't want it in your repository? Then you can remove doxygen,
breathe and certain files from your repository:

*Hint*: After you have successfully deleted the C++ parts of the repository,
you can make the documentation without them, e.g. ``cd ./docs && mkdir build && make html``.

To delete the C++ parts of the repository:

#. Delete the files/directories:

   .. code-block:: console

     $ rm -rf libs/src_cxx docs/source/src_cxx docs/doxygen CMakeLists.txt tests/test_mock_cxx.py

#. In the file ``docs/source/index.rst`` delete: ``src_cxx/index`` from the toctree.

#. In the file ``.github/workflows/CI.yaml`` delete:

   .. code-block:: yaml

     - name: Build Pybind11 module for C++ code
       run: |
         cmake -S ./ -B ./build
         cd build && make

   and

   .. code-block:: yaml

      - name: Install Doxygen
        run: /usr/share/miniconda/envs/goodsciproj_env/bin/doxygen --version
        shell: bash
      - name: Generate Doxygen Documentation
        run: |
          cd docs &&
          mkdir build &&
          mkdir build/doxygen &&
          /usr/share/miniconda/envs/goodsciproj_env/bin/doxygen doxygen/doxygen.dox
        shell: bash

#. In ``docs/source/conf.py`` delete ``"breathe"`` from ``extenstions`` and

   .. code-block:: python

     # Integrate doxygen with sphinx via breathe
     breathe_projects = {
         "src_cxx": "../build/doxygen/xml/",
     }

     breathe_default_project = "proj"


#. In ``.pre-commit-config.yaml`` delete:

   .. code-block:: yaml

     -   repo: https://gitlab.com/daverona/pre-commit/cpp
         rev: 0.8.0
         hooks:
         -   id: cpplint
             args: [--linelength=100, "--filter=-runtime/references,-readability/braces,-build/include,-build/c++11"]
             types_or: [c, c++, cuda]

#. In ``requirements.txt`` delete ``breathe``.

#. In ``environment.yaml`` delete ``- conda-forge::doxygen>=1.10.0``


Pybind11
########
https://github.com/pybind/pybind11/
