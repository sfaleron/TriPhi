
from __future__  import division
from __future__  import print_function
from __future__  import absolute_import

from simplesvg   import SVGStack, SVG, filled_polygon
from src         import defaults, tileOpts, redraw

from src.keyattr import KeywordToAttr
from src.layers  import mixed_up_triangles
from src.tiles   import TileSet, adjacent_tiles
from src.math    import inner, pi


def make_tile(stk, path, opts):

    stk.push_layer('tile {}{}'.format(path, 'x' if opts.flip else '+'), True)

    mixed_up_triangles(stk,
        opts.tri1, opts.tri2, opts.tri3, opts.colors,
            opts.flip, name='squat', noLayer=True, **opts.attrs.pgon)

    mixed_up_triangles(stk,
        opts.tri1, opts.tri2, opts.tri3, opts.colors,
            opts.flip, name='slim', noLayer=True, **opts.attrs.pgon)

    stk.add(filled_polygon(opts.tri2, opts.colors.bg, **opts.attrs.pgon))

    stk.pop()


def _make_tiles(stk, tiles, n, noFlips, path, opts):
    if n == 0:
        return

    for ii,tri in enumerate(adjacent_tiles(opts.tri1, opts.side)):
        opts_ = opts.copy()
        path_ = path+str(ii)

        if not noFlips:
            opts_.flip = not opts_.flip

        a,b,c = tri
        d,e,f, g,h,i = inner(a,b,c, opts_.flip)

        opts_.points.update(zip(
            ('A','B','C', 'D','E','F', 'G','H','I'),
            ( a,  b,  c,   d,  e,  f,   g,  h,  i) ) )

        if tri not in tiles:
            tiles.add(tri)
            make_tile(stk, path_, opts_)

        _make_tiles(stk, tiles, n-1, noFlips, path_, opts_)


def make_tiles(n, noFlips=False, flipZero=False, sideLength=None, rotate=0, turns=0, opts=None):
    if opts is None:
        opts = defaults.copy()
        opts.update(tileOpts)

    if flipZero:
        opts.flip = not opts.flip

    if sideLength:
        opts.side = sideLength

    opts.rotate = rotate or turns*pi/6

    redraw(opts)

    stk = SVGStack(SVG('TriPhi Tiles'))

    make_tile(stk, '0', opts)

    tiles = TileSet(opts.tri1)

    _make_tiles(stk, tiles, n, noFlips, '0', opts)

    stk[0].update(viewBox='{:f} {:f} {:f} {:f}'.format(*tiles.geo))

    return stk

def make_nonnegative(typ):
    def new(cls, valueIn):
        valueOut = typ(valueIn)

        if valueOut<0:
            raise ValueError('Non-negative values only.')

        return typ.__new__(cls, valueOut)

    return type('NonNegative_'+typ.__name__, (typ,), dict(__new__=new))

# more args: side length, orientation: 0:up, 30:right, 60:down, 90:left
# take integer, enforce multiple of 30, or multiply by 30? turns:n seems good!
# not affected by flip!

if __name__ == '__main__':
    from argparse import ArgumentParser

    psr = ArgumentParser()
    psr.add_argument(  'depth',      type=make_nonnegative(int))
    psr.add_argument( '-noFlips',    action='store_true')
    psr.add_argument( '-flipZero',   action='store_true')
    psr.add_argument('--turns',      type=int, default=0)
    psr.add_argument('--rotate',     type=float, default=0)
    psr.add_argument('--sideLength', type=make_nonnegative(float))

    argsKw = vars(psr.parse_args())

    argsKw['rotate'] *= pi/180

    depth  = argsKw.pop('depth')

    print(make_tiles(depth, **argsKw))
