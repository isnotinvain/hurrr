'''
==================================================================
hurrr by Alex Levenson

Utilities for vectors of any length

All methods return the same type as the first vector parameter
This means that the first vector parameter must have a constructor that accepts a generator

All methods that act on more than one vector require that they all be the same length

It is my *untested* theory that these methods are less efficient than the analogous ones
found in 2d.py (whcih work only on 2-dimensional vectors)
=================================================================
'''

import itertools
import math

def add(vec1, vec2):
  """
  returns the elementwise sum of vec1 and vec2
  vec1 and vec2 must be the same length
  return type matches vec1
  vec1 must have a constructor that accepts a generator
  """
  __assertVecSameLength(vec1, vec2)
  return type(vec1)(p[0] + p[1] for p in itertools.izip(vec1,vec2))

def distance(vec1, vec2):
  '''
  return: the distance between vec1 and vec2
  '''
  return math.sqrt(distance2(vec1, vec2))

def distance2(vec1, vec2):
  '''
  return: the distance**2 between vec1 and vec2
  faster than distance above, use for comparisons
  '''
  __assertVecSameLength(vec1, vec2)
  return sum((p[0]-p[1])**2 for p in itertools.izip(vec1, vec2))

def midPt(vec1, vec2):
  '''
  return: the midpoint of the line segment from vec1 --> vec2
  return type matches vec1
  vec1 must have a constructor that accepts a generator
  '''
  __assertVecSameLength(vec1, vec2)
  return type(vec1)((p[0]+p[1])/2.0 for p in itertools.izip(vec1, vec2))

def ceil(vec, ceil):
  '''
  return: vec if the magnitude of vec is < ceil,
  otherwise vec scaled to have magnitude ceil
  return type matches vec
  vec must have a constructor that accepts a generator
  '''
  mag = magnitude(vec)

  if mag > ceil:
    f = float(ceil) / mag
    return type(vec)(x*f for x in vec)
  return vec

def scale(vec, mag):
  '''
  return: vec scaled to have magnitude mag
  return type matches vec
  vec must have a constructor that accepts a generator
  '''
  cmag = magnitude(vec)
  if cmag == 0:
    raise ValuError("Cannot scale a vector of zero magnitude")
  f = float(mag) / cmag
  return type(vec)(x*f for x in vec)

def magnitude(vec):
  '''
  return the magnitude of vec
  '''
  return math.sqrt(magnitude2(vec))

def magnitude2(vec):
  '''
  return the magnitude**2 of vec
  '''
  return sum(x**2 for x in vec)

def __assertVecSameLength(vec1, vec2):
  if not len(vec1) == len(vec2):
    raise Exception("Vectors not of the smame length")
