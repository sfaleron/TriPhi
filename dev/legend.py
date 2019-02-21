"""
"angles" angles a,b
"sides"  sides  a,b,c

nested svg should be avoided if possible

would a viewbox with relative sizes work better wrt nested transfomations?
yeah, use percentages.. can even move the origin to the center
dunno about flipping y, but that might be getting invasive

be interesting if that fixed the inkscape issues.. well, its more of an
"avoiding." better than a "workaround," for sure.


parts have width, height stated as attributes of svg element, so positioning
them relative to each other should be cake. the height/width of svg sets
the block of parent space that is occupied, so making a new svg with the
appropriate width/height would do the job. what about just a group?

not sure how to assemble in a reusable way.. that is a generally useful
problem to solve sometime. might need to process all at once when making
the unit pair. wrapping anything in a group makes it transformable, but
then there's nested transformations that are going to be tricky until
they aren't.
"""
