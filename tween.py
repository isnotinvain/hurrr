'''
==================================================================
hurrr by Alex Levenson

Utilities for tweening and easing and animating
=================================================================
'''
import itertools

def easeOut(current, target, smooth):
  '''
  Proportionally interpolate current towards target
  '''
  return current + (target - current) / smooth

def getTweenedVector(fromVec, toVec, numFrames):
  '''
  return: numFrames number of vectors, representing a tween from fromVec to toVec
  '''
  floatFrames = float(numFrames)

  tweenRect = list(fromVec)

  deltas = map(lambda x : x[1] - x[0], itertools.izip(fromVec, toVec))
  deltas = map(lambda x : x / floatFrames, deltas)

  frames = []
  for _ in xrange(numFrames - 1):
    tweenRect = map(lambda x: x[1] + deltas[x[0]], enumerate(tweenRect))
    frames.append(tuple(tweenRect))
  return frames