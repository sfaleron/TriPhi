External dependencies:

  - `Node.js`_

    + `MathJax-node`_
    + `ini`_

  - `Python`_ (2 or 3)

    + `six`_

Most build targets are included in the repository. They are text files, generally not
very long, and useful on their own. By their inclusion, a build environment is not
required in order to use them.

Rather than tracking these files, which could easily get messy, frozen versions are
kept in a tracked archive, ``build.zip``. This archive can be updated manually
for better control, or all targets at once by running ``bin/zipbuild.sh``.

.. _Node.js: https://nodejs.org/
.. _Python:  https://python.org/

.. _MathJax-node: https://github.com/mathjax/MathJax-node
.. _ini: https://github.com/npm/ini#readme
.. _six: https://pypi.org/project/six/
