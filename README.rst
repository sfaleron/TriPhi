
Creates the TriPhi figure used as my `avatar`_, and `explores`_ the underlying `math`_.

The inspiration came from a `page`_ at the "Interactive Mathematics Miscellany and Puzzles" `website`_. I also find `this one`_ satisfying, but the figure that is all
straight lines should be more recognizable when rendered at low resolution, as for
a favicon, for instance.

+---------------------------------------------------------------------------------------------------------------+
| Short Quick-browsing Guide                                                                                    |
+=================+=============================================================================================+
|``lib/``         |Geometric parameters in MathML rendered to SVG                                               |
+-----------------+---------------------------------------------------------------------------------------------+
|``svg/``         |SVG and PNG images                                                                           |
+-----------------+---------------------------------------------------------------------------------------------+
|``figure.py``    |Generates the TriPhi figure                                                                  |
+-----------------+---------------------------------------------------------------------------------------------+
|``unitpair.py``  |Generates an annotated diagram of the essential geometric parameters                         |
+-----------------+---------------------------------------------------------------------------------------------+
|``tiles.py``     |Recursively generates a tiling of the TriPhi figure                                          |
+-----------------+---------------------------------------------------------------------------------------------+
|``vertexdump.py``|Generates a uniform text dump of vertices, in four permutations, given settings in options.py|
+-----------------+---------------------------------------------------------------------------------------------+

Depends on:

  - `SimpleSVG`_, `attrs`_, `six`_
  - a couple of personal libraries I hope to have on GitHub soon

.. _avatar: https://github.com/sfaleron/TriPhi/blob/master/svg/figure.png
.. _explores: https://github.com/sfaleron/TriPhi/blob/master/svg/unitpair.png
.. _math: https://www.mathcha.io/editor/vEBYC1KFnvu2vIy2
.. _six: https://pypi.org/project/six/
.. _attrs: http://www.attrs.org/
.. _website: http://www.cut-the-knot.org/
.. _page: http://www.cut-the-knot.org/do_you_know/Buratino7.shtml
.. _this one: http://www.cut-the-knot.org/do_you_know/Buratino2.shtml
.. _SimpleSVG: https://github.com/sfaleron/SimpleSVG
