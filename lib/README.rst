
Render geometric parameters from MathML to SVG. `Source MathML`_ was
authored in and exported from the `Mathcha website`_.

Intended for integration into the unitpair image.

Most build targets are included in the repository. They are text files, generally not
very long, and useful on their own. By their inclusion, a build environment is not
required in order to use them.

Rather than tracking these files, which could easily get messy, frozen versions are
kept in a tracked archive, ``build.zip``. This archive can be updated manually
for better control, or all targets at once by running ``bin/zipbuild.sh``.

----

Dependencies:

  - `Node.js`_

    + `MathJax-node`_
    + `ini`_

  - `Python`_ (2 or 3)

    + `six`_


.. _Node.js: https://nodejs.org/
.. _Python:  https://python.org/

.. _Source MathML: https://www.mathcha.io/editor/vEBYC1KFnvu2vIy2
.. _Mathcha website: https://www.mathcha.io

.. _MathJax-node: https://github.com/mathjax/MathJax-node
.. _ini: https://github.com/npm/ini#readme
.. _six: https://pypi.org/project/six/
