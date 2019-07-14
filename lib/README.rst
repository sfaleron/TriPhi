External dependencies
---------------------

  - Node.js

    + MathJax-node

  - Python (2 or 3)

    + six

Most build targets are included in the repository. They are text files, generally not
very long, and useful on their own. By their inclusion, a build environment is not
required in order to use them.

Rather than tracking these files, which could easily get messy, frozen versions are
kept in a tracked archive, ``targets.zip``. This archive can be updated manually
for better control, or all targets at once by running ``bin/ziptargets.sh``.
