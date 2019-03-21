
# A couple of these functions expect Point arguments, and they won't work with
# other sequences or iterators. This is fine, as their scope is limited to this
# package.

from  __future__ import division
from  __future__ import absolute_import

from simplesvg.lib.math import (
    Point, midpoint, between, sqrt, pi,
    atan2, sin, cos, make_scaler, dist )


# Construct a figure like that at http://www.cut-the-knot.org/do_you_know/Buratino7.shtml
# our points are labeled counterclockwise, which doesn't always correspond to the diagram on this page
#
# Maybe later: http://www.cut-the-knot.org/do_you_know/Buratino2.shtml
#
# Not triangular, but also interesting: http://www.cut-the-knot.org/do_you_know/Buratino6.shtml


#############################################################
# Find the radius of the circumcircle for a given side length
#
# the Law of Cosines says
# a^2 + b^2 - 2*a*b*cos(C) = c^2
#
# c is the subtended chord, and one side of the triangle
# a and b are radii, and C is 120 degrees. easy-peasy!
#
# 2*r^2 + r^2 = s^2
# sqrt(3)*r = s
#
def outer(sideLength, rotate=0):
    """sideLength is in pixels, rotate in radians"""

    # side/sqrt(3), or half of the height of the triangle
    r = sideLength/sqrt(3)

    ## ?? IVY ?? ##
    pts = [ Point(r*cos(a), r*sin(a)) for a in [
        (2./3*i+.5)*pi+rotate for i in range(3)] ]

    xs, ys = zip(*pts)

    xmin = min(xs); xmax = max(xs)
    ymin = min(ys); ymax = max(ys)

    ## IVY ##
    transform = lambda p: Point(p.x-xmin, ymax-p.y)

    return tuple(map(transform, pts))


########################################################################
# Find the inner triangle with vertices on the sides of the first
# triangle, and the innermost triangle, whose vertices are the mid-
# points of the second.
#
# D is colinear with AB, and the length of BD is the
# outermost side length AB divided by phi.
#
# Yeah, it'd be nice to have phi fall out of some equations, rather
# than using it explicitly, but there's a geometric proof on the web
# page cited, and crunching it algebraicly would only result in ex-
# pressions equivalent to what is here. I haven't done it yet, but I
# would start by parameterizing the inner triangle by the position of
# one vertex along a side of the outer triangle and setting the mid-
# points of the inner triangle to be colinear with the appropriate
# vertex of the outer triangle.

# The vertices are labeled in counterclockwise order.
# Outer A,B,C: A at the apex and BC horizontal.
# Inner D,E,F: vertices on the sides of ABC; D opposite A, E:B, F:C.
# Innermost G,H,I: vertices on midpoints of DEF; G adjacent to A via a
# long inner segment, H:B, I:C

def inner(A, B, C, flip=False):

    invphi = 2/(1+sqrt(5))

    if flip:
        invphi = 1-invphi

    D = between(C, B, invphi)
    E = between(A, C, invphi)
    F = between(B, A, invphi)

    G = midpoint(E, F)
    H = midpoint(F, D)
    I = midpoint(D, E)

    return (D,E,F, G,H,I)


# Given two points defining a side, find the remaining vertices of
# the two equilateral triangles that share this side.
#
# Find the line perpendicular to the side, at its midpoint, and go along
# the line for sqrt(3)/2 times the side length units.
#
# y-y1=m*(x-x1)
# m = -1/((y2-y1)/(x2-x1))
#
# y = (x1-x2)(x-x3)/(y2-y1)+y3 (1)
#
# Equation of the circle centered on the midpoint with the radius desired
# 3/4*s^2 = (y-y3)^2+(x-x3)^2  (2)
#
# Substitute (1) for y, solve for x
#
# x = x3 +/- sqrt(3/4)*s*
#     (y2-y1)/sqrt(x1^2+x2^2+y1^2+y2^2 - 2*(x1*x2+y1*y2))
#
# Substitute into (1) and solve for y
#
# y = y3 -/+ sqrt(3/4)*s*
#     (x2-x1)/sqrt(x1^2+x2^2+y1^2+y2^2 - 2*(x1*x2+y1*y2))
#
# It's worth pointing out there's no possible zeros in denominators here!
#
# At least if pt1 and pt2 are not the same point. Horizontal and vertical
# sides work fine. This is the only condition (among real numbers) for
# x1^2+x2^2+y1^2+y2^2 = 2*(x1*x2+y1*y2), according to Wolfram Alpha.
#
def triangles_from_side(pt1, pt2, sideLength=None):
    """Given two points defining a side, find the remaining vertices of
    the two equilateral triangles that share this side. A bit of
    calculating can be averted if the side length is handy when calling,
    or the third argument can be used to find isoceles triangles rather
    than equilateral. The height of the triangles is sqrt(3)/2*sideLength.

    Returns two A,B,C triples, in counterclockwise order, in the same
    manner as two calls to outer()."""

    midPt   = midpoint(pt1, pt2)

    if sideLength is None:
        # sideLength is a sqrt, makes sense to combine radicals
        a,b = 1, (pt1.x-pt2.x)**2 + (pt1.y-pt2.y)**2
    else:
        a,b = sideLength, 1

    k = a/2 * sqrt(3*b / (
        pt1.x**2 + pt2.x**2 + pt1.y**2 + pt2.y**2 - 2*(pt1.x*pt2.x + pt1.y*pt2.y)))

    pt3a = Point(midPt.x - (pt2.y-pt1.y)*k, midPt.y + (pt2.x-pt1.x)*k)
    pt3b = Point(midPt.x + (pt2.y-pt1.y)*k, midPt.y - (pt2.x-pt1.x)*k)

    return (make_ccw([pt1,pt2,pt3a], midPt), make_ccw([pt1,pt2,pt3b], midPt))


## ?? IVY ?? ##
def make_ccw(pts, ctr):
    return tuple(zip(*sorted(
        [(pt, atan2(pt.y-ctr.y, pt.x-ctr.x)) for pt in pts], key=lambda x:x[1]) ))[0]
