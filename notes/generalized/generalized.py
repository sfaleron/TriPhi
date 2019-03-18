
from __future__ import print_function
from __future__ import division

from math import acos, pi, sqrt, sin, cos

from collections import namedtuple

import sys

Point = namedtuple('Point', 'x y')

q = Point(-1, 0)
s = Point( 1, 0)

dist = lambda p1,p2: sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)

def disp_parms(b, theta):
    a = 1

    apex = Point(b*cos(theta), b*sin(theta))

    x = dist(apex, q)
    y = dist(apex, s)

    Q3 = acos((a**2 + b**2 - x**2) / (2*a*b)) / pi*180
    Q2 = acos((a**2 + x**2 - b**2) / (2*a*x)) / pi*180
    Q1 = acos((b**2 + x**2 - a**2) / (2*b*x)) / pi*180

    S3 = acos((a**2 + b**2 - y**2) / (2*a*b)) / pi*180
    S2 = acos((a**2 + y**2 - b**2) / (2*a*y)) / pi*180
    S1 = acos((b**2 + y**2 - a**2) / (2*b*y)) / pi*180

    print('--------------------------------------')
    print('      1st       2nd       quot    inv')
    print('ab {:7.3f}   {:7.3f}   {:7.3f}   {:5.3f}'.format(a,b, b/a, a/b))
    print('xy {:7.3f}   {:7.3f}   {:7.3f}\n'.format(x,y, y/x))
    print('    squat     slim      apex')
    print('1  {:7.3f}   {:7.3f}   {:7.3f}'.format(Q1, S1, Q1+S1))
    print('2  {:7.3f}   {:7.3f}'.format(Q2, S2))
    print('3  {:7.3f}   {:7.3f}'.format(Q3, S3))


def match_angles(theta):
    c = cos(theta)

    x = sqrt(c**2+1)
    y1, y2 = x-c, x+c

    y1 = sqrt(2*c*(c - sqrt(c**2 + 1)) + 1)
    y2 = sqrt(2*c*(c + sqrt(c**2 + 1)) + 1)

    if c<0:
        y1, y2 = y2, y1

    return y1, y2


scale  = 240
width  = int(5.1*scale)
height = int(1.7*scale)

from simplesvg.lib.math import Point

def xform(pt):
    return Point(pt.x + width/2, height*.9 - pt.y)

def make_images(fnhead, theta):
    from PIL import Image, ImageDraw

    b1, b2 = match_angles(theta)

    o = xform(Point( 0, 0))
    q = xform(Point(-1, 0)*scale)
    s = xform(Point( 1, 0)*scale)

    b1, b2 = match_angles(theta)
    b3, b4 = match_angles(pi-theta)

    for b,a,tail in [
        (b1,    theta, 'angl-'), (b2,    theta, 'angl+'),
        (b3, pi-theta, 'comp-'), (b4, pi-theta, 'comp+')]:

        img    = Image.new('RGBA', (width, height))
        draw   = ImageDraw.Draw(img)
        apex   = xform(Point(cos(a), sin(a))*b*scale)

        draw.polygon([apex, q, s])
        draw.line(   [apex, o])

        img.save('{}{}.png'.format(fnhead, tail))

if __name__ == '__main__':
    # Command-line parameters:
    #   length angle : display stats, with a given b
    #          angle : display stats, with complementary b's defined by the angle
    #   fnhead angle :   make images, with complementary b's defined by the angle

    import sys

    args = sys.argv[1:]
    a    = float(args.pop())/180*pi

    if args:
        try:
            b = float(args[0])
            disp_parms(b,  a)
        except ValueError:
            make_images(args[0], a)
    else:
        b1, b2 = match_angles(a)

        disp_parms(b1, a)
        disp_parms(b2, a)
