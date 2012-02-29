# hurrr by Alex Levenson

import math
import angle
import vec

def movePt(pt, angle, distance):
  '''
  move a point by a ray
  return: a new point that has been moved
  '''
  cAngle = angle.normalizeAngle(angle)
  delta = vec.scale((-math.sin(cAngle), math.cos(cAngle)), distance)
  return vec.add(pt, delta)

def slope(pt1, pt2):
  '''
  return: the slope between pt1 and pt2 or inf for vertical lines
  '''
  if pt1[0] - pt2[0] == 0: return float('inf')
  return (pt1[1] - pt2[1]) / (pt1[0] - pt2[0])