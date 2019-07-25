
The "canonical" vector images produced by this package reside here. They can
be rebuilt by invoking ``make`` without explicit targets. If `Inkscape`_ is
installed, bitmaps may be obtained by ``make bitmaps``. Only PNG bitmaps
are supported; Inkscape does not support exporting to JPEG on the command line,
and it would `not be a good image format here`__ anyway, although it offers some
metadata opportunities PNG does not.

The other formats are easy to obtain by replacing the ``-e`` switch with
the indicated alternate. See Inkspace's man page or other reference for
available formats and their switch(es).

----

Many alternatives to Inkscappe were tried, none of which were satisfactory.
The bad ones didn't respect the stylesheet or produced garbled text, and the
better ones managed to miss the underlines somehow, even when being rendered
in a headless browser instance which rendered perfectly in the usual
standalone configuration.

A comprehensive evaluation of available solutions was attempted, but it
certainly wasn't exhaustive. I'm open to suggestions that are:

- Freely available
- Cross platform
- Preferably can run locally with a minimum of bulky or installed-for-all-users
  dependencies, but a reliable, public API service would be considered. \*

The user is left with three options:

- Abstain; vector graphics are the future!
- Use Inkscape; it's a handy tool and open source. The recent releases don't
  even crash regularly on Windoze anymore!

  + Win7, at least. One never knows with win10..

- Manual conversion. There is no shortage of web-based or local tools that
  feature SVG to "x" possibilities.

----

\* I found a few public APIs with free plans. One seemed less restrictive and
had the most overall developer-friendly feel: `cloudconvert`_. I tried them
out, and got byte-wise identical output to Inkscape's! I haven't tried the
others, but cloudconvert worked well for me. Give them a try if Inkscape is
less preferred than third-party-over-internet-service and the (ample for most)
limitations on their free service.


__  SkipJPEG_

.. _Inkscape: https://inkscape.org/
.. _skipJPEG: https://en.wikipedia.org/wiki/Portable_Network_Graphics#JPEG
.. _cloudconvert: https://cloudconvert.com/
