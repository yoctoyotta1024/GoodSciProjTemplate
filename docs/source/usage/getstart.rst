.. _getstart:

Getting Started
===============

Clone GoodSciProjTemplate's GitHub repository:

.. code-block:: console

  $ git clone https://github.com/yoctoyotta1024/GoodSciProjTemplate.git

and then create an environment with the necessary dependencies installed (e.g. using micromamba,
or conda as listed in the environment.yaml):

.. code-block:: console

  $ micromamba create -f environment.yaml
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
  a. delete ``git@github.com:yoctoyotta1024/GoodSciProjTemplate.git`` from your remote with ``git remote remove origin``,
  b. add your repository: ``git remote add origin [git@github.com:your_repository_ssh.git]``,
#. Make yourself the ``github.repository_owner`` who triggers GitHub's CI to publish documentation (see `.github/workflows/CI.yaml`).
#. Set your documentation to deploy using the `/(root)` folder of your gh-pages branch (see instructions `here <https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site>`_)
#. Switch to a new branch using git and start customising the template...
  a. ``git switch -c [branch_name]``,
  b. [make changes],
  c. ``git add -p`` (accept / decline changes),
  d. ``git commit -m "<type>[optional scope]: <description>"`` (see the `conventional commits guidelines <https://www.conventionalcommits.org>`_),
  e. ``git push``.

Necessary second steps:
#######################

#. Create and push your first version tag to the repository:
  a. ``git tag -a v0.0.0 -m "init repo"``,
  b. ``git push --tags``.
#. Make the project name yours instead of "GoodSciProjTemplate".
#. Make the citation and liscence refer to you instead of me.
#. Corect the repository name and its owner for GitHub (e.g. in the CI.yaml and cog.toml).
#. Write a new README.md (shorter is generally better) and include a link to your documentation in it.
#. Change the GitHub links in the .rst files to the correct ones for your GitHub repository (*hint*: you find these files in the `docs` directory).
#. Commit and push your changes to a branch of your GitHub repository (not main!).
#. Create a pull request and accept it if your CI succeeds to merge/rebase your changes to the main branch of your remote (GitHub) repository.
#. Update your local main branch and any other local branches your have.
  a. ``git switch main && git pull``,
  b. ``git switch [other_branch] && git rebase main``.
#. Setup (or delete) cocogitto
#. Setup (or delete) Python bindings for C++

Some suggested third steps:
###########################

#. Make the release/version yours instead of "0.0.0".
#. Change the names of the C++ and Python package names in the `libs` directory (maybe you also prefer to call "libs" "src"?)
#. If you made a C++ library, set your ```INPUT``` in `doxygen.dox` and your ``breathe_projects`` and/or ``default_breathe_projects`` in `conf.py` to match the name of the new C++ library.
#. Make a new Python or C++ module/subpackage (include docstrings and write unit tests in the `tests` directory!).
#. Create an associated .rst file for your new module/subpackage (somewhere in the `docs/source` directory).
#. Add the path to your new .rst file to the contents of the ``.. toctree::`` in `index.rst`.
#. Push your changes to a branch of your GitHub repository (not main!).
#. Create a pull request and accept it if your CI succeeds to merge your changes to the main branch of your remote (GitHub) repository.
#. Be proud of your new code with documentation and tests!

Want more ideas?!
#################
Have you thought about adding contributors, acknowledgements, more Python and/or
other requirements/environments, more CI or pre-commit tasks, and an automatic file header
generator? Maybe you've noticed this repository uses 
`conventional commit <https://www.conventionalcommits.org/en/v1.0.0/>`_
messages to enable `cocogitto<https://docs.cocogitto.io/>`_'s automatic version control?
Or maybe you should ponder all this over a cup of tea and some biscuits...

A Note on Commiting Large Files:
################################
This project forbids you from commiting and pushing large files such as Jupyter notebooks
(.ipynb files) and images (e.g. .png files) to your repository. Such actions are highly
discouraged and usually a sign that you are doing something wrong. If you want to use Jupyter
notebooks, consider using the `Jupyter Book <https://jupyterbook.org/en/stable/intro.html>`_
extension of Sphinx to store your notebooks as markdown files. At the very least, you should scrub
notebooks before committing them because you do not want to destory the power of git diff by making
it start comparing Jupyter notebook hashes.
