
from  __future__ import division
from  __future__ import print_function
from  __future__ import absolute_import

from   simplesvg import SVGStack, filled_polygon, Path, Line

from src.options import defaults
from src.math    import Point, sqrt
from src.keyattr import AttribItem, KeywordToAttr, kw2aDec


@kw2aDec
class Points(KeywordToAttr):
    _attribs = map(AttribItem, ['common', 'apex', 'slim', 'squat'])

if __name__ == '__main__':
    pts   = Points(common=Point(0,0), squat=Point(-1,0), slim=Point(1,0),
        apex=Point(-(1+sqrt(5))/4, -(sqrt(15)+sqrt(3))/4) )

    pgonAttrs = defaults.attrs.pgonAttrs
    lineAttrs = defaults.attrs.lineAttrs.copy()

    lineAttrs['stroke-width'] = '.02px'


    # horizontal, vertical margins = .15, .1
    # apex y-coordinate is -1.401, convenient!
    stk = SVGStack(viewBox='{:f} {:f} {:f} {:f}'.format(-1.15, -1.5, 2.3, 1.6))

    stk.add(filled_polygon((pts.common, pts.apex, pts.squat),
        defaults.colors.squat, **pgonAttrs)

    stk.add(filled_polygon((pts.common, pts.apex, pts.slim),
        defaults.colors.slim, **pgonAttrs)
