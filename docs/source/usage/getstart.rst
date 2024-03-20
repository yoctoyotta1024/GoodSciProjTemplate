.. _getstart:

Getting Started
===============

Clone GoodSciProjTemplate's GitHub repository:

.. code-block:: console

  $ git clone https://github.com/yoctoyotta1024/GoodSciProjTemplate.git

and then create an environment with the necessary dependencies installed (using micromamba, mamba
or conda as listed in the environment.yml):

.. code-block:: console

  $ micromamba env create -f environment.yml
  $ micromamba activate scienv

Finally install the pre-commit hooks:

.. code-block:: console

  $ pre-commit install

which will be used when you try to commit something or you execute ``pre-commit run``. You can learn
more about the powers of pre-commit from `their documentation: <https://pre-commit.com>`_.

That's it, you're done! But maybe now you want to customise the project and push it to your own
GitHub repo...

Necessary first steps:
###########################

#. Create an empty GitHub repository and push your new project to it.
#. Make yourself the ``github.repository_owner`` who triggers GitHub's CI to publish documentation (see `.github/workflows/CI.yml`).
#. Set your documentation to deploy using the `/(root)` folder of your gh-pages branch (see instructions `here <https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site>`_)
#. Checkout to a new branch using git and start customising the template...

Necessary second steps:
#######################

#. Make the project name yours instead of "GoodSciProjTemplate".
#. Make the release/version yours instead of "0.0.0".
#. Make the citation and liscence refer to you instead of me.
#. Write a new README.md (shorter is generally better) and include a link to your documentation in it.
#. Change the GitHub links in the .rst files to the correct ones for your GitHub repository (*hint*: you find these files in the `docs` directory).

Some suggested third steps:
###########################
#. Change the names of the C++ and Python package names in the `libs` directory (maybe you also prefer to call "libs" "src"?)
#. If you made a C++ library, set your ```INPUT``` in `doxygen.dox` and your ``breathe_projects`` and/or ``default_breathe_projects`` in `conf.py` to match the name of the new C++ library.
#. Make a new Python or C++ module/subpackage (include docstrings and write unit tests in the `tests` directory!).
#. Create an associated .rst file for your new module/subpackage (somewhere in the `docs/source` directory).
#. Add the path to your new .rst file to the contents of the ``.. toctree::`` in `index.rst`.
#. Push your changes to a branch of your GitHub repository (not main!).
#. Create a pull request (and accept it if your tests pass) to merge your changes with the main branch of your GitHub repository.
#. Be proud of your new code with documentation and tests.

Want more ideas?!
#################
Have you thought about adding contributors, acknowledgements, more Python and/or
other requirements / enviroments, more CI or pre-commit tasks, and an automatic file header
generator? Or maybe you should ponder it all over a cup of tea and some biscuits...

A Note on Commiting Large Files:
################################
This project does not forbid you from commiting and pushing large files such as Jupyter notebooks
(.ipynb files) and images (e.g. .png files) to your repository. However, such actions are highly
discouraged and usually a sign that you are doing something wrong. If you want to use Jupyter
notebooks, consider using the `Jupyter Book <https://jupyterbook.org/en/stable/intro.html>`_
extension of Sphinx to store your notebooks as markdown files. At the very least, you should scrub
notebooks before committing them because you do not want to destory the power of git diff by making
it start comparing Jupyter notebook hashes.
