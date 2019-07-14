
The final products of this build system are ``table.svg`` ``steps.svg``, one
of which be selected (first by link, perhaps permanently later) to be
``relationships.svg``, which is used as an input to the ``unitpair.py``
program that produces ``unitpair.svg``, as one of the primary SVG produced
by this software package.

The targets of the build system have many intermediates. Most have utility
beyond assembly of the final products, so are retained. A classification system
has been arranged to aid in understanding the build process and for later
referral. All are valid MathML or SVG and are either in the ``src`` or
``intermediates`` directories. Each change in classification is a step along
the build process, in the order shown below.

1. *raw* / ``r`` files have the extension ``*.in.mml`` are the "source" files,
   are the only XML files that are intended for direct editing, and are located
   in the ``src`` directory. An exception is the derived file ``lengths.in.mml``
   that is a stacking of the ``lengthL`` and ``lengthR`` source files. It is
   found in the ``intermediates`` directory with the other intermediate steps.

2. *mml* / ``m`` files are *raw* / ``r`` files with some substitutions concerning
layout and mathematical symbols are made.

3. *svg* / ``s`` files are *mml* / ``m`` files rendered as SVG.

Two other files are concerned:
- ``parameters`` is an INI-style configuration file that defines the parameters
  used in assembly of the final products. It contains comments that should
  clarify its usage.

- ``intermediates/nsDecl`` is a derived file that caches state used when parsing
  the *raw* / ``r`` files.
