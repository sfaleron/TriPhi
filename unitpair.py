
from   __future__  import division
from   __future__  import print_function
from   __future__  import absolute_import

# Group and Style are not used, but either might find easy application

from     simplesvg import (
    SVGStack, Polygon, Group, Style,
    filled_polygon, Line, SVG, TSpan )

from  simplesvg.lib.math.decorations import (
    HatchDecorations, ArcDecorations, LineLabel, AngleLabel )

from src.options   import defaults
from src.math      import Point, sqrt, make_scaler, pi
from src.keyattr   import AttribItem, KeywordToAttr, kw2aDec

from functools     import partial

import os.path     as osp

SCL = 200

SANEIVY = False

@kw2aDec
class Points(KeywordToAttr):
    _attribs = map(AttribItem, ['common', 'apex', 'slim', 'squat'])

Scale = make_scaler(SCL)

if __name__ == '__main__':
    Point_ = lambda a,b: SCL*Point(a+1.1, b+1.48)

    ## ?? IVY ?? ##
    pts = Points(common=Point_(0,0), squat=Point_(-1,0), slim=Point_(1,0),
        apex=Point_(-(1+sqrt(5))/4, -(sqrt(15)+sqrt(3))/4) )

    pgonAttrs = {'stroke-width' : '0px', 'fill-opacity' : .7}
    lineAttrs = {'stroke' : 'black', 'stroke-width' : Scale(.0065).px, 'fill-opacity' : 0}
    decAttrs  = {'stroke' : 'black', 'stroke-width' : Scale(.0040).px}

    arcs    =   ArcDecorations(radius=Scale(0.075), spacing=Scale(0.015))
    hatches = HatchDecorations(length=Scale(0.075), spacing=Scale(0.020))

    # horizontal, vertical margins = .1, .1
    # apex y-coordinate is -1.401, convenient!
    stk = SVGStack( SVG('Unit Pair',
        docFlags={'inkOffsetFix'}, width=Scale(2.2), height=Scale(1.6)) )

    # relative to svg directory
    stk.baseNode.add_styleSheet('../fonts/stylesheet.css')

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

    # Below this line, the resulting SVG starts to look different in Inkscape
    # vs browsers.

    # SVG exported from Mathcha looks good in firefox and opera (distinct
    # engines), both standalone and embedded, but is an indecipherable mess
    # in inkscape, both standalone and embedded.

    # the dx, dy adjustments have a dramatically different affect. Inkscape
    # diminishes them quite a bit vs the browsers. Intuitively, the
    # browsers are getting it right, but (not) getting the transformations
    # straight in my mental model seems to be a recurring SVG problem. Maybe
    # it's just an inkscape problem?

    # Fixed dx/dy by including an optional "fix" that adds them to the
    # corresponding coordinate. Makes animation a little harder, but not by much.

    # The mathcha SVG is still yucky, though.

    Desc  = partial( LineLabel, **{'class': 'desc', 'font-size': Scale(.05)})
    NameL = partial( LineLabel, **{'class': 'name', 'font-size': Scale(.05)})
    Large = partial( LineLabel, **{'class': 'name', 'font-size': Scale(.13)})

    NameA = partial(AngleLabel,            **{'class': 'name', 'font-size': Scale(.05)})
    ShowA = partial(AngleLabel, show=True, **{'class': 'name', 'font-size': Scale(.05)})

    stk.add( Desc(pts.apex,   pts.squat,  'exterior short',    invert=True, dy=Scale(-.03), dx=Scale(0) ))
    stk.add(NameL(pts.apex,   pts.squat,  'q3',                invert=True, dy=Scale( .07), dx=Scale(0) ))
    stk.add( Desc(pts.apex,   pts.slim,   'exterior long',  dy=Scale(-.03), dx=Scale(-.23) ))
    stk.add(NameL(pts.apex,   pts.slim,   's3',             dy=Scale( .07), dx=Scale(-.23) ))
    stk.add( Desc(pts.apex,   pts.common, 'interior long',  dy=Scale(-.03), dx=Scale(-.05) ))
    stk.add(NameL(pts.apex,   pts.common, 'q2',             dy=Scale( .07), dx=Scale(  .2) ))
    stk.add(NameL(pts.apex,   pts.common, 's2',             dy=Scale(-.03), dx=Scale(  .2) ))

    stk.add( Desc(pts.common, pts.slim,   'interior short',              dy=Scale( .08) ))
    stk.add( Desc(pts.common, pts.squat,  'interior short', invert=True, dy=Scale( .08) ))
    stk.add(NameL(pts.common, pts.squat,  'q1',             invert=True, dy=Scale(-.06) ))
    stk.add(NameL(pts.common, pts.slim,   's1',                          dy=Scale(-.06) ))

    stk.add( NameA(pts.apex, pts.common, pts.squat,    Scale(.2), 'Q1', rotate=pi/75))
    stk.add(NameA(pts.squat, pts.common, pts.apex,          None, 'Q2', dx=Scale(.07), dy=Scale(-.03) ))

    stk.add(NameA(pts.apex, pts.common,  pts.slim, Scale(.24), 'S1', rotate=pi/45))


    if SANEIVY:
        stk.add(ShowA(pts.common, pts.apex, pts.squat,    Scale(.1), 'Q3', rotate=0))
    else:
        stk.add(NameA(pts.common, pts.apex, pts.squat, Scale(-.135), 'Q3', rotate=-pi/18))

    if SANEIVY:
        stk.add(ShowA( pts.slim, pts.common, pts.apex, Scale(.05), 'S2', rotate=0 ))
    else:
        stk.add(NameA( pts.slim, pts.common, pts.apex, Scale(.05), 'S2', dx=Scale(-.16), dy=Scale(-.03) ))

    stk.add(NameA(pts.common, pts.apex,  pts.slim,       None, 'S3', dx=Scale( .04), dy=Scale(-.03) ))


    uline = partial(TSpan, **{'text-decoration': 'underline'})

    txt = stk.add(Large(pts.common, pts.squat, invert=True, dy=Scale(-.22), dx=Scale(-.08) ))
    txt.add_many('S', uline('q'), 'uat')

    txt = stk.add(Large(pts.common, pts.slim,               dy=Scale(-.22), dx=Scale(-.27) ))
    txt.add_many(uline('S'), 'lim')

    print(stk)
