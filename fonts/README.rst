
Roughly follows this blog `post`_:

See also a very useful `resource`_ at MDN.

The free fonts were acquired from the `site`_ hosting the generator tool mentioned in the blog entry. The ones chosen (regular and italic variants) for this application were from the `Sinkin Sans`_ family. Love the word play!

These were uploaded back again to obtain the webfont package. This comes with a lot of files, some diagnostic, and several different webfont formats. For this application, only the ``.woff`` formatted webfonts and the stylesheet were retained. For broader compatibility, a different selection could be made.

The stylesheet was also trimmed and modified. I removed reference to webfont formats that were not retained, and adjusted the properties so that the fonts were more organized. The stylesheet comes with a distinct ``font-family`` value for each webfont. By resetting ``font-family`` and ``font-style``, the intuitive arrangement was obtained. ``font-weight`` is another property that could easily be relevant in some applications.

Probably not trouble for the CSS masters out there, but I encountered some gotchas that others of a similar experience level might be stumped for a while on:

- When setting the ``src`` to a filesystem location, I found ``url()`` worked, while ``local()`` did not. Presumably, ``local()`` refers to system fonts.
- The path to the font is relative to the CSS file, not the working directory or other usual suspect.
- This is also the case for the CSS file relative to the SVG file.

Less a gotcha then advice for handling them: Once the stylesheet is correctly loaded, the font parameters may be set by keyword arguments or with inline CSS via the ``style`` keyword argument. You may already know this, but it's one of the assumptions that's easiest to question when one becomes frustrated by failures that might be tricky to plumb if one isn't practiced in the art of using their browser's developer's features.

.. _post: http://schepers.cc/svg-webfonts
.. _site: https://www.fontsquirrel.com/
.. _Sinkin Sans: https://www.fontsquirrel.com/fonts/sinkin-sans
.. _resource: https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face
