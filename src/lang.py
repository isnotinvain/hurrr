'''
==================================================================
hurrr by Alex Levenson

Utilities for working with the python language
=================================================================
'''
import itertools

def isIterable(item):
  '''
  return wether item is iterable
  '''
  try:
    iter(item)
  except TypeError:
    return False
  return True

def ensureIterable(item, message="Must be iterable"):
  '''
  raises a TypeError if item is not iterable (with optional message)
  '''
  if not isIterable(item): raise TypeError(message)

class Enum(object):
  '''
  A simple Enum implementation

  useage:
    verbs = Enum.new("HURPING", "SKURPING", "DURPING")
    currentState = verbs.HURPING
    if currentState == verbs.HURPING:
      print "hurping!"

    OR

    colors = Enum.new(RED=(255, 0, 0), GREEN=(0,255,0), BLUE=(0, 0, 255))
    color = colors.RED

  This is based on an answer to a stack overflow question written by:
  http://stackoverflow.com/users/7980/alec-thomas

  I couldn't find a way to contact him so: thanks Alec!
  '''

  @classmethod
  def new(cls, *seq, **named):
    if seq and named:
      raise ValueError("Must supply either sequence or named, not both!")
    if not seq and not named:
      raise ValueError("Must supply either sequence or named!")
    if seq:
      if len(seq) != len(set(seq)):
        raise ValueError("Duplicate keys in enum:" + str(seq))
      named = dict(itertools.izip(seq, xrange(len(seq))))
    else:
      if len(named) != len(set(named.itervalues())):
        raise ValueError("Duplicate values in enum:" + str(named))
    return type('Enum', (cls,), named)