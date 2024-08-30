Commit Messages and Versioning
==============================

This repository uses cocogitto, a Command-Line Interface (like git) and a toolbox for the
Conventional Commits and Semver specifications. The basic idea is that by writing commit messages
which always obey the conventional commit message structure cocogitto can automatically
perform version bumping and generate a changelog for you.

The conventional commit message structure is:

  <type>[optional scope]: <description>

  [optional body]

  [optional footer(s)]

but you can find more information on the conventional commit website (see below).

Setting-Up Cocogitto
####################
This repository enables a few of cocogitto's optional features (see ``cog.toml``).
One is that the changelog is generated via GitHub's CI relative to the first tag called "v0.0.0". You
therefore need to delete any existing ``CHANGELOG.md`` and then add this tag to your GitHub repository,
either on GitHub or by pushing the tag from your local repository, e.g.

a. ``git tag -a v0.0.0 -m "init repo"``,
b. ``git push --tags``.

You also need to modify some settings in the ``cog.toml`` file under ``[changelog]``:
    - ``repository = "[your_repo_name]"``
    - ``owner = "[your_github_username]"``
    - ``authors = [{ username = "[your_github_username]", signature = "[your_name]" }]``

Deleting Cocogitto
##################
To delete cocogitto, simply remove the ``cog.toml`` and ``.github/workflows/cocogitto.yaml`` files
from your repository. You might also want to delete the ``CHANGELOG.md`` if you've generated one.

Cocogitto
#########
https://docs.cocogitto.io/

Conventional Commits
####################
https://www.conventionalcommits.org/
