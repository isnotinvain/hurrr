import math
import Box2D as box2d
import pygame
import hurrr.gui
import hurrr.physics
import hurrr.twod

class Game(object):
  def __init__(self):
    self.window = hurrr.gui.Window(updateFunc=lambda: self.update(), drawFunc=lambda screen:self.draw(screen), screenToWorldRatio=25.0)
    self.window.run(setupWindow=lambda w: self.setupWindow(w))

  def setupWindow(self, window):
    self.world = hurrr.physics.Simulator(dimensions=((0,0),window.camera.toWorld(window.size)))
    self.body = self.world.addBody((5,5), None)
    bodyCircleDef = box2d.b2CircleDef()
    bodyCircleDef.radius = 0.5
    bodyCircleDef.localPosition.Set(0.0, 0.0)
    bodyCircleDef.density = 1.0
    bodyCircleDef.restitution = 0.6
    bodyCircleDef.friction = 0.5
    self.body.CreateShape(bodyCircleDef)
    self.body.SetMassFromShapes()

  def update(self):
    self.world.step()
    return True

  def draw(self, screen):
    wCenter = self.body.GetWorldCenter().tuple()
    center = map(lambda x : int(x), self.window.camera.toScreen(wCenter))
    pygame.draw.circle(screen, (255, 153, 0), center, int(self.window.camera.scalarToScreen(0.5)))
    cAngle = self.body.GetAngle()
    vec = -1 * math.sin(cAngle), math.cos(cAngle)
    x, y = hurrr.twod.scale(vec, 0.5)
    x += wCenter[0]
    y += wCenter[1]
    end = self.window.camera.toScreen((x, y))
    pygame.draw.line(screen, (204,102,102), center, end, 2)

Game()