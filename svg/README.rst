
The "canonical" vector images produced by this package reside here. They can
be rebuilt by invoking ``make`` without explicit targets. If `Inkscape`_ is
installed, bitmaps may be obtained by ``make bitmaps``. Only PNG bitmaps
are supported; Inkscape does not support export to JPEG on the command line,
and it would `not be a good image format here`__, although it offers some
metadata opportunities PNG does not.

The other formats are easy to obtain by replacing the ``-e`` switch with
the indicated alternate. See Inkspace's man page or other reference for
available formats and their switch(es).

----
Many alternates were tried, none of which were satisfactory. The bad ones
didn't respect the stylesheet or produced garbled text, and the better ones
managed to miss the underlines somehow, even when being rendered in a headless
browser instance which rendered perfectly in the usual standalone configuration.
I leave the user with three options:

- Abstain; vector graphics are the future!
- Use Inkscape; it's a handy tool and open source. The recent releases don't
  even crash regularly on Windoze anymore!
- Manual conversion. There is no shortage of web-based or local tools that
  feature SVG to "x" possibilities.

__ SkipJPEG_

.. _Inkscape: https://inkscape.org/
.. _skipJPEG: https://en.wikipedia.org/wiki/Portable_Network_Graphics#JPEG
