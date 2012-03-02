'''
==================================================================
hurrr by Alex Levenson

Utilities for tweening and easing and animating
=================================================================
'''

def easeOut(current, target, smooth):
  '''
  Proportionally interpolate current towards target
  '''
  return current + (target - current) / smooth