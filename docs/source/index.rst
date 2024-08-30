.. GoodSciProjTemplate documentation master file, based off sphinx-quickstart.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to GoodSciProjTemplate's Documentation!
===============================================

.. note::
   Please consider that this project is under active development
   and our documentation is a work in progress.

   This documentation is built from the latest code in the main branch of the repository.
   It does not necessarily reflect a released version, and there may be short-commings when compared
   to the on-going code development. If you have queries related to
   this or if there is anything you wish to report please please :ref:`contact us! <contact>`.

This library aims to be a template to make it easy and quick for you to incorporate best coding and
scientific practises into your GitHub repositories. The template demonstrates:

* what to include in file headers
* how to document your Python and C++ code
* how to make tests for your code (using pytest)
* how to liscence your code
* how to write a citation for your code
* things to include in a .gitignore file (e.g. large files like jupyter notebooks)
* how to list the requirements of your code (i.e. dependencies) in an environment YAML file
* how to use pre-commit for code checks, linting and formatting (see https://pre-commit.com/)
* how to use continuous integration (CI) to run pytest and publish documentation on GitHub (see https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration)
* how to write conventional commit messages
* how to use conventional commits and CI for automatic version control on GitHub

To (locally) reproduce this project, simply clone the repository. You will need to setup an
environment with the dependencies installed and then run ``pre-commit install`` but other than
that everything should work out of the box and you can now run & have fun with the project...
If not, please raise an issue on the GitHub repository.

Time to get involved! Check out the :doc:`getting started page<usage/getstart>`.

Contents
--------
.. toctree::
   :maxdepth: 1

   usage/getstart
   usage/ourdocs
   usage/ourtests
   src_py/index
   src_cxx/index

   GitHub Repo <https://github.com/yoctoyotta1024/GoodSciProjTemplate.git>
   usage/contributing
   usage/contact
   references

Questions?
----------
Yes please! Simply :ref:`contact us! <contact>`

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
