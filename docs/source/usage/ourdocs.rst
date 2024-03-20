Our Docs
========

Sphinx builds this documentation and we integrate C++ documentation built by Doxygen using the
Breathe extension.

You can build the documentation locally by building the Doxygen .xml files
followed by the Sphinx .html files, e.g.

.. code-block:: console

  $ cd ./docs && mkdir build && mkdir build/doxygen
  $ doxygen doxygen/doxygen.dox && make html

which you can then view in your preferred browser e.g.

.. code-block:: console

  $ open build/html/index.html

Viewing Documentation Files on a Remote Machien Using your Local Browser
------------------------------------------------------------------------
Let's say you're working on a remote machine (e.g. Levante) and have made some changes to the
documentation in a branch of your repository. After you built the documentation via

.. code-block:: console

  $ cd ./docs && mkdir build && make html

You probably now want to open a brower and have a look at the updated docs. However,
``open build/html/index.html`` won't work because the ``index.html`` file is on the remote sever
not your local file system. Here is a good way to solve this problem exampled on Levante:

#. Open up a new terminal on your local machine

#. SSH to Levante with local port forwarding enabled:

    .. code-block:: console

      $ ssh -L 8765:localhost:8765 <userid>@levante.dkrz.de

#. Enter the directory than contains the ``index.html`` file and create an http server from it.

    .. code-block:: console

      $ cd docs/build/html/
      $ python -m http.server 8765

#. Open the server on your preferred browser e.g. https://localhost:8765

In the command above the '``8765``'s in ``8765:localhost:8765`` are port numbers. They can be pretty
much any number above 1024, but if someone else is already using the port number you choose then it
won't work for you. In that case simply try a different number / numbers e.g. ``9090:localhost:9090``.

Further Resources
-----------------

Sphinx
######
https://www.sphinx-doc.org/en/master/

Breathe
#######
https://breathe.readthedocs.io/en/latest/

Doxygen
#######
https://www.doxygen.nl

Contributing to Our Documentation
---------------------------------
If you would like to contribute to the documentation, have questions or would like clarification or
more detail on a particular topic, please :ref:`contact us! <contact>`.
