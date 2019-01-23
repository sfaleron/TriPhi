
from  __future__ import division
from  __future__ import print_function
from  __future__ import absolute_import

from simplesvg     import SVGStack, filled_polygon, Path, Line, Polygon
from simplesvg.lib import TickDecorations, ArcDecorations

from src.options import defaults
from src.math    import Point, sqrt
from src.keyattr import AttribItem, KeywordToAttr, kw2aDec

SCL = 200

@kw2aDec
class Points(KeywordToAttr):
    _attribs = map(AttribItem, ['common', 'apex', 'slim', 'squat'])

if __name__ == '__main__':
    Point_ = lambda a,b:SCL*(Point(a+1.1,b+1.5))

    pts = Points(common=Point_(0,0), squat=Point_(-1,0), slim=Point_(1,0),
        apex=Point_(-(1+sqrt(5))/4, -(sqrt(15)+sqrt(3))/4) )

    pgonAttrs = {'stroke-width' : '0', 'fill-opacity' : .7}
    lineAttrs = {'stroke' : 'black',   'stroke-width' : .0065*SCL, 'fill-opacity' : 0}
    decAttrs  = {'stroke' : 'black',   'stroke-width' : .004* SCL}

    arcs  =  ArcDecorations(radius=0.08*SCL, spacing=0.015*SCL)
    ticks = TickDecorations(length=0.08*SCL, spacing=0.02*SCL)

    # horizontal, vertical margins = .1, .1
    # apex y-coordinate is -1.401, convenient!
    stk = SVGStack(width=2.2*SCL, height=1.6*SCL)

    stk.add(filled_polygon((pts.common, pts.apex, pts.squat),
        defaults.colors.squat, **pgonAttrs))

    stk.add(filled_polygon((pts.common, pts.apex, pts.slim),
        defaults.colors.slim, **pgonAttrs))

    stk.add(Polygon((pts.apex, pts.slim, pts.squat), **lineAttrs))
    stk.add(Line(pts.apex, pts.common, **lineAttrs))

    stk.add(ticks(pts.common, pts.slim, **decAttrs))
    stk.add(ticks(pts.common, pts.squat, **decAttrs))

    stk.add(arcs(pts.slim, pts.apex, pts.common, **decAttrs))
    stk.add(arcs(pts.apex, pts.squat, pts.common, **decAttrs))

    stk.add(arcs(pts.apex, pts.slim, pts.squat, n=2, radius=0.12*SCL, **decAttrs))
    stk.add(arcs(pts.common, pts.apex, pts.squat, n=2, **decAttrs))

    # labels might be nice to have, and possibly a little box off to the side
    # with the side ratios and maybe also some angle values. Maybe area too.

    print(stk)
