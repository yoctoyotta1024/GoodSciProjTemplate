.. _getstart:

Getting Started
===============

Clone GoodSciProjTemplate's GitHub repository:

.. code-block:: console

  $ git clone https://github.com/yoctoyotta1024/GoodSciProjTemplate.git

and then create an environment with the necessary dependencies installed (e.g. using micromamba,
or conda as listed in the environment.yaml):

.. code-block:: console

  $ micromamba env create -f environment.yaml
  $ micromamba activate goodsciproj_env

Finally install the pre-commit hooks:

.. code-block:: console

  $ pre-commit install

which will be used when you try to commit something or you execute ``pre-commit run``. You can learn
more about the powers of pre-commit from `their documentation: <https://pre-commit.com>`_.

That's it, you're done! But maybe now you want to customise the project and push it to your own
GitHub repo...

Making the Project Your Own
===========================

Necessary first steps:
###########################

#. Create an empty GitHub repository and set the remote url for your new project to it.
    a. delete ``git@github.com:yoctoyotta1024/GoodSciProjTemplate.git`` from your remote with ``git remote remove origin``
    b. add your repository: ``git remote add origin [git@github.com:your_repository_ssh.git]``

#. Make yourself the ``github.repository_owner`` who triggers GitHub's CI to publish documentation (see `.github/workflows/CI.yaml`).
#. Set your documentation to deploy using the `/(root)` folder of your gh-pages branch (see `instructions for gitHub publishing <https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site>`_).
#. Switch to a new branch using git and start customising the template...

Necessary second steps:
#######################

#. Create the 0th version tag in the remote repository:
    a. ``git tag -a v0.0.0 -m "init repo"``
    b. ``git push --tags``
    c. ``git branch -M main``
    d. ``git push -u origin main``

#. Delete GoodSciProjTemplate's CHANGELOG.md ``rm CHANGELOG.md``.
#. Make the project name yours instead of "GoodSciProjTemplate".
#. Make the citation and liscence refer to you instead of me.
#. Corect the repository name and its owner for GitHub (e.g. in the CI.yaml).
#. Write a new README.md (shorter is generally better) and include a link to your documentation in it.
#. Change the GitHub links in the .rst files to the correct ones for your GitHub repository
   (*hint*: you find these files in the `docs` directory).
#. Commit and push your changes to a branch of your GitHub repository (not main!).
#. Create a pull request and accept it if your CI succeeds in order to to merge/rebase your
   changes to the main branch of your remote (GitHub) repository.
#. Update your local main branch and any other local branches your have.
#. Setup (or delete) cocogitto (see :doc:`cocogitto`).
#. Build (or delete) C++ code in the repository (see :doc:`pybind11`).


Some suggested third steps:
###########################

#. Make the release/version yours instead of "0.0.0".
#. Change the names of the C++ and Python package names in the `libs` directory (maybe you also prefer to call "libs" "src"?)
#. If you made a C++ library, set your ```INPUT``` in `doxygen.dox` and your ``breathe_projects`` and/or ``default_breathe_projects`` in `conf.py` to match the name of the new C++ library.
#. Make a new Python or C++ module/subpackage (include docstrings and write unit tests in the `tests` directory!).
#. Create an associated .rst file for your new module/subpackage (somewhere in the `docs/source` directory).
#. Add the path to your new .rst file to the contents of the ``.. toctree::`` in `index.rst`.
#. Push your changes to a branch of your GitHub repository (not main!).
#. Create a pull request and accept it if your CI succeeds to merge your changes to the main
   branch of your remote (GitHub) repository.
#. Be proud of your new code with documentation and tests!


Want more ideas?!
#################

Have you thought about adding contributors, acknowledgements, more Python and/or
other requirements/environments, more CI or pre-commit tasks, and an automatic
file header generator? Maybe you've noticed this repository uses conventional
commits to enable cocogitto's automatic version control?
Or maybe you should ponder all this over a cup of tea and some biscuits...


A Note on Commiting Large Files:
################################

This project forbids you from commiting and pushing large files such as Jupyter notebooks
(.ipynb files) and images (e.g. .png files) to your repository. Such actions are highly
discouraged and usually a sign that you are doing something wrong. If you want to use Jupyter
notebooks, consider using the `Jupyter Book <https://jupyterbook.org/en/stable/intro.html>`_
extension of Sphinx to store your notebooks as markdown files. At the very least, you should scrub
notebooks before committing them because you do not want to destory the power of ``git diff`` by
making it start comparing Jupyter notebook hashes.

A Standard Git + GitHub Workflow
################################

Always keep your local main branch up to date with its remote version! Everytime you start work,
you should perform ``git switch main`` then ``git pull`` (or ``git fetch`` and ``git merge``).

#. Before you start making any change to your repo, you should first branch off your main branch:
    a. ``git switch main``
    b. ``git switch -c [branch_name]``
#. Make the changes you want and stage them with:
    a. ``git add -p`` (accept / decline changes)
#. Commit your changes (frequently!!) with:
    a. ``git commit -m "<type>[optional scope]: <description>"``
    b. See `conventional commit guidelines <https://www.conventionalcommits.org>`_ for writing good commit messages
#. Push your changes to your remote repository with ``git push``.
#. Create a pull request to merge/rebase your changes to your remote main branch.
#. Delete your local (and remote) branch after your pull request is accepted:
    a. ``git branch -d [branch_name]``
#. Start a new branch from main to make further changes.

If you happen to be working on a branch at the same time that changes to the main branch occur,
make sure to keep your branch up-to-date! The more your branch differs from main, the more likely
you will encounter merge conflicts (not fun!). Keep your branches up to date by keeping your local
main branch up-to-date and then keeping your branches up-to-date with your local main branch. E.g.

a. ``git switch main`` then ``git pull``
b. ``git switch [branch_name]`` then ``git rebase main``
