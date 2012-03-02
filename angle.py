'''
==================================================================
hurrr by Alex Levenson

Utilities for working with angles in radians
=================================================================
'''

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