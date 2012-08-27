'''
==================================================================
hurrr by Alex Levenson

A 2D camera abstraction that handles:
  * Converting screen to world coordinates
  * Positional Offset
  * Zoom

This is essentially the glue between rendering an simulation
=================================================================
'''
import hurrr

class Camera(object):
  '''
  A 2D camera abstraction that handles:
    * Converting screen to world coordinates
    * Positional Offset
    * Zoom
  '''
  def __init__(self, screenToWorldRatio, screenIsInverted, screenSize, pos):
    '''
    screenToWorldRatio: how many screen units per world unit
                        in the case of pygame and box2d
                        this would be pixels per meter
    '''
    self.screenToWorldRatio = screenToWorldRatio
    self.screenIsInverted = screenIsInverted
    self.screenSize = screenSize
    self.pos = (0, 0)

  def toScreen(self, pt):
    x,y = hurrr.twod.sub(pt, self.pos)
    x,y = self.scalarToScreen(x), self.scalarToScreen(y)
    if self.screenIsInverted:
      y = self.screenSize[1] - y
    return x,y

  def toWorld(self, pt):
    x,y = pt
    if self.screenIsInverted:
      y = self.screenSize[1] - y
    x,y = self.scalarToWorld(x), self.scalarToWorld(y)
    return hurrr.twod.add(pt, self.pos)

  def scalarToScreen(self, scalar):
    return scalar * self.screenToWorldRatio

  def scalarToWorld(self, scalar):
    return scalar / self.screenToWorldRatio