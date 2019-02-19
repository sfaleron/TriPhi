
from  __future__ import division
from  __future__ import print_function
from  __future__ import absolute_import

from simplesvg     import SVGStack, SVG, filled_polygon, Line, Polygon, TSpan
from simplesvg.lib import HatchDecorations, ArcDecorations, LineLabel

from src.options import defaults
from src.math    import Point, sqrt, make_scaler
from src.keyattr import AttribItem, KeywordToAttr, kw2aDec

from functools   import partial

SCL = 200

@kw2aDec
class Points(KeywordToAttr):
    _attribs = map(AttribItem, ['common', 'apex', 'slim', 'squat'])

Scale = make_scaler(SCL)

if __name__ == '__main__':
    Point_ = lambda a,b: SCL*Point(a+1.1, b+1.48)

    pts = Points(common=Point_(0,0), squat=Point_(-1,0), slim=Point_(1,0),
        apex=Point_(-(1+sqrt(5))/4, -(sqrt(15)+sqrt(3))/4) )

    pgonAttrs = {'stroke-width' : '0px', 'fill-opacity' : .7}
    lineAttrs = {'stroke' : 'black', 'stroke-width' : Scale(.0065).px, 'fill-opacity' : 0}
    decAttrs  = {'stroke' : 'black', 'stroke-width' : Scale(.0040).px}

    arcs    =   ArcDecorations(radius=Scale(0.075), spacing=Scale(0.015))
    hatches = HatchDecorations(length=Scale(0.075), spacing=Scale(0.020))

    # horizontal, vertical margins = .1, .1
    # apex y-coordinate is -1.401, convenient!
    stk = SVGStack(SVG('Unit Pair', width=Scale(2.2), height=Scale(1.6)))

    stk.add(filled_polygon((pts.common, pts.apex, pts.squat),
        defaults.colors.squat, **pgonAttrs))

    stk.add(filled_polygon((pts.common, pts.apex, pts.slim),
        defaults.colors.slim, **pgonAttrs))

    stk.add(Polygon((pts.apex, pts.slim, pts.squat), **lineAttrs))
    stk.add(Line(pts.apex, pts.common, **lineAttrs))

    stk.add(hatches(pts.common, pts.slim, **decAttrs))
    stk.add(hatches(pts.common, pts.squat, **decAttrs))

    stk.add(arcs(pts.slim, pts.apex, pts.common, **decAttrs))
    stk.add(arcs(pts.apex, pts.squat, pts.common, **decAttrs))

    stk.add(arcs(pts.apex, pts.slim, pts.squat, n=2, radius=Scale(0.12), **decAttrs))
    stk.add(arcs(pts.common, pts.apex, pts.squat, n=2, **decAttrs))

    kw = {'font-size': '85%'}

    stk.add(LineLabel(pts.apex,   pts.squat,  'exterior short', invert=True, dy=Scale(-.03), **kw ))
    stk.add(LineLabel(pts.apex,   pts.slim,   'exterior long',               dy=Scale(-.03), **kw ))
    stk.add(LineLabel(pts.apex,   pts.common, 'interior long',               dy=Scale(-.03), dx=Scale(-.1), **kw ))

    stk.add(LineLabel(pts.common, pts.slim,   'interior short',              dy=Scale(.08), **kw ))
    stk.add(LineLabel(pts.common, pts.squat,  'interior short', invert=True, dy=Scale(.08), **kw ))

    kw = {'font-size': '85%', 'font-style': 'oblique'}

    stk.add(LineLabel(pts.apex,   pts.squat,  'q3', invert=True, dy=Scale(.06), **kw ))
    stk.add(LineLabel(pts.apex,   pts.slim,   's3',              dy=Scale(.06), **kw ))

    stk.add(LineLabel(pts.apex,   pts.common, 'q2',              dy=Scale( .06), dx=Scale(.45), **kw ))
    stk.add(LineLabel(pts.apex,   pts.common, 's2',              dy=Scale(-.03), dx=Scale(.45), **kw ))

    stk.add(LineLabel(pts.common, pts.squat,  'q1', invert=True, dy=Scale(-.06), **kw ))
    stk.add(LineLabel(pts.common, pts.slim,   's1',              dy=Scale(-.06), **kw ))

    kw = {'font-size': '200%'}
    tspan = partial(TSpan, **{'text-decoration': 'underline'})

    e = stk.add(LineLabel(pts.common, pts.squat, invert=True, dy=Scale(-.24), dx=Scale(-.15), **kw ))
    e.add_many('S', tspan('q'), 'uat')

    e = stk.add(LineLabel(pts.common, pts.slim,               dy=Scale(-.24), dx=Scale(-.55), **kw ))
    e.add_many(tspan('S'), 'lim')


    # labels might be nice to have, and possibly a little box off to the side
    # with the side ratios and maybe also some angle values. Maybe area too.

    print(stk)
