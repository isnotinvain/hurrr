import math
import random
import Box2D as box2d
import pygame
import hurrr.gui
import hurrr.physics
import hurrr.twod
import hurrr.control.prim as prim
import hurrr.angle
class Bot(object):
  def __init__(self, world, pos, target, color):
    self.body = world.addBody(pos, None)
    bodyCircleDef = box2d.b2CircleDef()
    bodyCircleDef.radius = 0.5
    bodyCircleDef.localPosition.Set(0.0, 0.0)
    bodyCircleDef.density = 1.0
    bodyCircleDef.restitution = 0.6
    bodyCircleDef.friction = 0.5
    self.body.CreateShape(bodyCircleDef)
    self.body.SetMassFromShapes()
    self.pid = prim.TwodPIDController(kp=1.0, kd=600.0, ki=5.0, kiDamp=0.9)
    self.target = target
    self.color = color

  def draw(self, screen, camera):
    wCenter = self.body.GetWorldCenter().tuple()
    center = map(lambda x : int(x), camera.toScreen(wCenter))
    pygame.draw.circle(screen, self.color, center, int(camera.scalarToScreen(0.5)))
    pygame.draw.circle(screen, self.color, hurrr.twod.ints(camera.toScreen(self.target)), int(camera.scalarToScreen(0.1)))
    cAngle = self.body.GetAngle()
    vec = -1 * math.sin(cAngle), math.cos(cAngle)
    x, y = hurrr.twod.scale(vec, 0.5)
    x += wCenter[0]
    y += wCenter[1]
    end = camera.toScreen((x, y))
    pygame.draw.line(screen, (204,102,102), center, end, 2)

  def update(self):
    f = self.pid.getControlSignal(self.body.GetWorldCenter(), self.target)
    self.body.ApplyForce(f, self.body.GetWorldCenter())

class Game(object):
  def __init__(self):
    self.window = hurrr.gui.Window(updateFunc=lambda: self.update(), drawFunc=lambda screen:self.draw(screen), screenToWorldRatio=25.0)
    self.window.run(setupWindow=lambda w: self.setupWindow(w))

  def setupWindow(self, window):
    worldDims = map(window.camera.scalarToWorld, window.size)
    worldDims = (worldDims[0] + 10, worldDims[1] + 10)
    self.world = hurrr.physics.Simulator(dimensions=((-10,-10), worldDims), gravity=(0.0, 0.0))
    self.botHold = Bot(self.world, (5, 5), (10,10), (255, 153, 0))
    self.attack = []
    for i in xrange(3):
      self.attack.append(Bot(self.world, (15, 15), (10,10), (0, 153, 0)))

  def update(self):
    self.botHold.target = self.window.camera.toWorld(pygame.mouse.get_pos())
    self.botHold.update()

    for a in self.attack:
      angle = hurrr.twod.angleBetweenPts(a.body.GetWorldCenter(), self.botHold.body.GetWorldCenter())
      a.target = hurrr.twod.movePt(self.botHold.body.GetWorldCenter(), -angle, 1)
      a.update()

    self.world.step()
    return True

  def draw(self, screen):
    self.botHold.draw(screen, self.window.camera)
    for a in self.attack:
      a.draw(screen, self.window.camera)

Game()