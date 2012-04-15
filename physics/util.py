'''
==================================================================
hurrr by Alex Levenson

Utilities for Box2D
=================================================================
'''
import Box2D as box2d

def bodiesAtPoint(world, pt, includeStatic=False, includeSensor=False, maxBodies=1000):
  '''
  Find up to maxBodies located at pt
  '''
  # modified from the Elements source (formerly: http://elements.linuxuser.at)
  # see NOTE above
  # thanks guys!
  sx, sy = pt
  f = 0.01
  aabb = box2d.b2AABB()
  aabb.lowerBound.Set(sx - f, sy - f);
  aabb.upperBound.Set(sx + f, sy + f);
  amount, shapes = world.Query(AABB, maxBodies)
  bodies = set()
  if amount == 0:
    return bodies
  else:
    for s in shapes:
      if s.IsSensor() and not includeSensor: continue
      body = s.GetBody()
      if not includeStatic:
        if body.IsStatic() or body.GetMass() == 0.0:
          continue

      if s.TestPoint(body.GetXForm(), (sx, sy)):
        bodies.append(body)
    return bodies

def bodiesInRegion(world, region, maxBodies=1000):
  '''
  Find up to maxBodies located in a region
  '''
  left, top = region[0]
  right, bottom = region[1]

  aabb = box2d.b2AABB()
  aabb.lowerBound.Set(left, bottom)
  aabb.upperBound.Set(right, top)
  count, shapes = world.Query(aabb, maxBodies)
  bodies = set()
  for shape in shapes:
    bodies.add(shape.GetBody())
  return bodies

def b2PolyToPoints(shape):
  '''
  convert a b2Poly into a list of its points
  '''
  points = []
  for i in xrange(shape.GetVertexCount()):
    pt = box2d.b2Mul(shape.GetBody().GetXForm(), shape.getVertex(i))
    points.append(pt)
  return points

def stopBody(body):
  '''
  Stop a bodies linear and angular motion
  '''
  body.SetLinearVelocity((0, 0))
  body.SetAngularVelocity(0)
