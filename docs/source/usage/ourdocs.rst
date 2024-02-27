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

  $ open build/html/index.htm

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
#################################
If you would like to contribute to the documentation, have questions or
would like clarification or addition to the documentation about
a particular topic, please :ref:`contact us! <contact>`.
