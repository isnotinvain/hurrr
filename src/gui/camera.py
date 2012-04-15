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
class Camera(object):
  '''
  A 2D camera abstraction that handles:
    * Converting screen to world coordinates
    * Positional Offset
    * Zoom
  '''
  def __init__(self, screenToWorldRatio, screenIsInverted, screeHeight):
    '''
    screenToWorldRatio: how many screen units per world unit
                        in the case of pygame and box2d
                        this would be pixels per meter
    '''
    self.screenToWorldRatio = screenToWorldRatio
    self.screenIsInverted = screenIsInverted
    self.screenHeight = screeHeight
    self.zoom = 1.0
    self.pos = (0,0)
    if self.screenIsInverted and not self.screenHeight:
      raise ValueError("You must provide a screenHeight if the screen is inverted")

  def toScreen(self, pt):
    x,y = self.scalarToScreen(pt[0]), self.scalarToScreen(pt[1])
    if self.screenIsInverted:
      y = self.screenHeight - y
    return x,y

  def toWorld(self, pt):
    x,y = self.scalarToWorld(pt[0]), self.scalarToWorld(pt[1])
    if self.screenIsInverted:
      y = self.screenHeight - y
    return x,y

  def scalarToScreen(self, scalar):
    return scalar * self.screenToWorldRatio * self.zoom

  def scalarToWorld(self, scalar):
    return scalar / (self.screenToWorldRatio * self.zoom)