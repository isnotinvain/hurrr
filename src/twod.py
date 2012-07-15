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

sqrt2 = math.sqrt(2.0)

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

def manhattanDistance(pt1, pt2, blockSize, roundFunc=math.floor):
   '''
   return: the distance between pt1 and pt2 using the manhattan method
           (distance along a grid, think walking along city blocks)
           blockSize: is the length of a block (blocks treated as squares)
           roundFunc: default math.floor (ignore partial blocks), use math.ceil
                      to count partial blocks
   '''
   x1,y1 = pt1
   x2,y2 = pt2
   xdist = roundFunc(float(abs(x1-x2)) / blockSize)
   ydist = roundFunc(float(abs(y1-y2)) / blockSize)
   return int((xdist + ydist) * blockSize)

def chessBoardDistance(pt1, pt2, blockSize, roundFunc=math.floor):
  '''
  return: the distance between pt1 and pt2 using the chessBoard method
          (distance along a grid, diagonal movement allowed, think the King in chess)
          blockSize: is the length of a block (blocks treated as squares)
          roundFunc: default math.floor (ignore partial blocks), use math.ceil
                     to count partial blocks
  '''
  x1,y1 = pt1
  x2,y2 = pt2
  xdist = roundFunc(float(abs(x1-x2)) / blockSize)
  ydist = roundFunc(float(abs(y1-y2)) / blockSize)
  diag = min(xdist, ydist)
  straight = (xdist + ydist)
  return (sqrt2*blockSize) * diag + blockSize * (straight - 2*diag)

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

def ints(vec):
  '''
  maps int() over all elements of vec
  '''
  return (int(vec[0]), int(vec[1]))

def floats(vec):
  '''
  maps float() over all elements of vec
  '''
  return (float(vec[0]), float(vec[1]))

def movePt(pt, ang, distance):
  '''
  move a point by a ray
  return: a new point that has been moved
  '''
  cAngle = angle.normalizeAngle(ang)
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

def ceilRect(size, maxSize, returnFactor=False):
  """
  @return a rectangle scaled to fit inside maxSize while preserving aspect ratio
  if returnFactor is True return the scaling factor and the new rectangle
  """

  width, height = size
  maxWidth, maxHeight = maxSize
  if (maxWidth, maxHeight) == (0, 0) or (width, height) == (0, 0): return (0, 0)
  wfactor, hfactor = 1.0, 1.0

  if width > maxWidth: wfactor = float(maxWidth) / width
  if height > maxHeight: hfactor = float(maxHeight) / height

  factor = min(wfactor, hfactor)

  size = (width * factor, height * factor)

  if not returnFactor:
    return size
  else:
    return size, factor

def rectContainsRect(rect1, rect2):
  """
  return: whether rect1 contains rect2
  """
  x1, y1, w1, h1 = rect1
  x2, y2, w2, h2 = rect2

  if x2 >= x1 and y2 >= y1 and x2 <= x1 + w1 and y2 <= y1 + h1 and x2 + w2 <= x1 + w1 and y2 + h2 <= y1 + h1:
    return True
  return False

def rectContainsPt(pt, rect):
  '''
  return: whether rect contains pt
  '''
  px, py = pt
  rx, ry, w, h = rect
  return px >= rx and px <= rx + w and py >= ry and py <= ry + h

def normalizeRect(pt1, pt2):
  '''
  return the rectange formed by pt1 and pt2 as (leftBottom, topRight)
  '''
  lx = min(pt1[0], pt2[0])
  ly = min(pt1[1], pt2[1])
  ux = max(pt1[0], pt2[0])
  uy = max(pt1[1], pt2[1])
  return ((lx,ly), (ux,uy))

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

# Some polygon magic, thanks to John W. Ratcliff on www.flipcode.com
# (triangleContainsPt, polySnip, and decomposePoly): I wrote these a long time ago
# I don't remember where the algorithms for them came from, but I think it was the flipcode
# article above
def triangleContainsPt(pt,triangle):
  '''
  return: whether pt is inside triangle
  '''
  ax = triangle[2][0] - triangle[1][0]
  ay = triangle[2][1] - triangle[1][1]
  bx = triangle[0][0] - triangle[2][0]
  by = triangle[0][1] - triangle[2][1]
  cx = triangle[1][0] - triangle[0][0]
  cy = triangle[1][1] - triangle[0][1]
  apx= pt[0] - triangle[0][0]
  apy= pt[1] - triangle[0][1]
  bpx= pt[0] - triangle[1][0]
  bpy= pt[1] - triangle[1][1]
  cpx= pt[0] - triangle[2][0]
  cpy= pt[1] - triangle[2][1]

  aCROSSbp = ax*bpy - ay*bpx
  cCROSSap = cx*apy - cy*apx
  bCROSScp = bx*cpy - by*cpx
  return aCROSSbp >= 0.0 and bCROSScp >= 0.0 and cCROSSap >= 0.0

def __polySnip(vertices,u,v,w,n):
  '''
  I have no idea what this does, it's used by decomposePoly
  '''
  EPSILON = 0.0000000001

  Ax = vertices[u][0]
  Ay = vertices[u][1]

  Bx = vertices[v][0]
  By = vertices[v][1]

  Cx = vertices[w][0]
  Cy = vertices[w][1]

  if EPSILON > (((Bx-Ax)*(Cy-Ay)) - ((By-Ay)*(Cx-Ax))):  return False

  for p in xrange(0,n):
    if p == u or p == v or p == w: continue
    Px = vertices[p][0];
    Py = vertices[p][1];
    if insideTriangle((Px,Py),((Ax,Ay),(Bx,By),(Cx,Cy))): return False;
  return True;

def decomposePoly(vertices):
  '''
  Decomposes a polygon into its triangles
  return: a lits of triangles
  '''
  vertices = list(vertices)
  n = len(vertices)
  result = []
  if(n < 3): return [] # not a poly!

  # force a counter-clockwise polygon
  if 0 >= polyArea(vertices):
    vertices.reverse()

  # remove nv-2 vertices, creating 1 triangle every time
  nv = n
  count = 2*nv # error detection
  m=0
  v=nv-1
  while nv>2:
    count -= 1
    if 0>= count:
      return [] # Error -- probably bad polygon

    # three consecutive vertices
    u = v
    if nv<=u: u = 0 # previous
    v = u+1
    if nv<=v: v = 0 # new v
    w = v+1
    if nv<=w: w = 0 # next

    if(__polySnip(vertices,u,v,w,nv)):

      # record this triangle
      result.append((vertices[u],vertices[v],vertices[w]))

      m+=1
      # remove v from remaining polygon
      vertices.pop(v)
      nv -= 1
      # reset error detection
      count = 2*nv
  return result
