'''
==================================================================
hurrr by Alex Levenson

Utilities for 2D math (points, lines, polygons, etc)

All methods return scalars or tuples
All methods work on indexable objects of length 2 or scalars where appropriate

It is my *untested* theory that these methods are more efficient than the analogous ones
found in vec.py (whcih work on n-dimensional vectors)
=================================================================
'''

import math
import angle

def add(vec1, vec2):
  """
  returns the elementwise sum of vec1 and vec2
  """
  return (vec1[0] + vec2[0], vec1[1] + vec2[1])

def distance(pt1, pt2):
  '''
  return: the distance between pt1 and pt2
  '''
  return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

def distance2(pt1, pt2):
  '''
  return: the distance**2 between pt1 and pt2
  faster than distance above, use for comparisons
  '''
  return ((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

def midPt(pt1, pt2):
  '''
  return: the midpoint of the line segment from pt1 --> pt2
  '''
  return ((pt1[0] + pt2[0]) / 2.0, (pt1[1] + pt2[1]) / 2.0)

def ceil(vec, ceil):
  '''
  return: vec if the magnitude of vec is < ceil,
  otherwise vec scaled to have magnitude ceil
  '''
  x, y = vec
  mag = math.sqrt(x ** 2 + y ** 2)
  if mag > ceil:
      x *= (ceil / mag)
      y *= (ceil / mag)
  return (x, y)

def scale(vec, mag):
  '''
  return: vec scaled to have magnitude mag
  '''
  x, y = vec
  if x == 0 and y == 0: return vec
  cmag = math.sqrt(x ** 2 + y ** 2)
  r = mag / cmag
  x *= r
  y *= r
  return (x, y)

def magnitude(vec):
  '''
  return the magnitude of vec
  '''
  return math.sqrt(magnitude2(vec))

def magnitude2(vec):
  '''
  return the magnitude**2 of vec
  '''
  return vec[0]**2 + vec[1]**2

def movePt(pt, angle, distance):
  '''
  move a point by a ray
  return: a new point that has been moved
  '''
  cAngle = angle.normalizeAngle(angle)
  delta = scale((-math.sin(cAngle), math.cos(cAngle)), distance)
  return add(pt, delta)

def slope(pt1, pt2):
  '''
  return: the slope between pt1 and pt2 or inf for vertical lines
  '''
  if pt1[0] - pt2[0] == 0: return float('inf')
  return (pt1[1] - pt2[1]) / (pt1[0] - pt2[0])

def angleBetweenPts(pt1, pt2):
    '''
    return: the angle between the line segment from pt1 --> pt2 and the x axis, from -pi to pi
    '''
    xcomp = pt2[0] - pt1[0]
    ycomp = pt1[1] - pt2[1]
    return math.atan2(ycomp, xcomp)

def constructTriangleFromLine(pt1, pt2):
  '''
  return: a list of points that describe an equilteral triangle around the segment from pt1 --> pt2
  '''
  halfHeightVector = (0.57735 * (pt2[1] - pt1[1]), 0.57735 * (pt2[0] - pt1[0]))
  pt3 = (pt1[0] + halfHeightVector[0], pt1[1] - halfHeightVector[1])
  pt4 = (pt1[0] - halfHeightVector[0], pt1[1] + halfHeightVector[1])
  return (pt2, pt3, pt4)

def polyArea(vertices):
    '''
    return: the area of the polygon described by vertices
    '''
    n = len(vertices)
    A = 0
    p = n - 1
    q = 0
    while q < n:
        A += vertices[p][0] * vertices[q][1] - vertices[q][0] * vertices[p][1]
        p = q
        q += 1
    return A / 2.0