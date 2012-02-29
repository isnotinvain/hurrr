# hurrr by Alex Levenson
import math

HALF_PI = math.pi / 2.0
PI = math.pi
TWO_PI = math.pi * 2

def normalizeAngle(angle):
  '''
  return: angle between 2pi and -2pi
  '''
  return angle - (int(angle / (TWO_PI)) * TWO_PI)

def normalizePositiveAngle(angle):
  '''
  return: angle between 0 and 2pi
  '''
  n = normalizeAngle(angle)
  if n < 0: n = TWO_PI - abs(n)
  return n

def betweenPts(pt1, pt2):
    '''
    return: the angle between the line segment from pt1 --> pt2 and the x axis, from -pi to pi
    '''
    xcomp = pt2[0] - pt1[0]
    ycomp = pt1[1] - pt2[1]
    return math.atan2(ycomp, xcomp)

def shortestTurn(current, desired):
    '''
    return: the least number of radians (+ or -) needed
    to get from current angle to desired angle (ie is it faster
    to turn left or turn right?)
    '''
    delta = desired - current
    if delta > PI:
        delta = -TWO_PI + delta
    elif delta < -PI:
        delta = TWO_PI + delta
    return delta