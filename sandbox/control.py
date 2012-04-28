import math
import Box2D as box2d
import pygame
import hurrr.gui
import hurrr.physics
import hurrr.twod
import hurrr.control.prim as prim
import hurrr.angle

class Game(object):
  def __init__(self):
    self.window = hurrr.gui.Window(updateFunc=lambda: self.update(), drawFunc=lambda screen:self.draw(screen), screenToWorldRatio=25.0)
    self.window.run(setupWindow=lambda w: self.setupWindow(w))

  def setupWindow(self, window):
    self.world = hurrr.physics.Simulator(dimensions=((0,0),window.camera.toWorld(window.size)), gravity=(3.0,-10.0))
    self.body = self.world.addBody((5,5), None)
    bodyCircleDef = box2d.b2CircleDef()
    bodyCircleDef.radius = 0.5
    bodyCircleDef.localPosition.Set(0.0, 0.0)
    bodyCircleDef.density = 1.0
    bodyCircleDef.restitution = 0.6
    bodyCircleDef.friction = 0.5
    self.body.CreateShape(bodyCircleDef)
    self.body.SetMassFromShapes()

    self.steps = 0
    self.pid = prim.TwodPIDController(prim.PIDController(1.0, 600, 0.5, 0.1), prim.PIDController(1.0, 300, 0.1, 0.8))
    self.apid = prim.PIDController(0.1, 300, 0.0, 0.1)
  def update(self):
    '''
    MI = 0.5 * self.body.GetMass() * 0.5 ** 2
    if self.steps == 0:
      torque = prim.torqueToSetVelocity(self.body.GetAngularVelocity(), hurrr.angle.TWO_PI, MI, 1.0/60)
      self.body.ApplyTorque(torque)
    elif self.steps == 60:
      torque = prim.torqueToSetVelocity(self.body.GetAngularVelocity(), hurrr.angle.HALF_PI, MI, 1.0/60)
      self.body.ApplyTorque(torque)
    '''
    '''
    if self.steps == 60:
      force = prim.forceToMove((10,10), self.body.GetMass(), self.body.GetLinearVelocity(), 1.0/60)
      self.body.ApplyForce(force, self.body.GetWorldCenter())

    if self.steps < 61:
      self.world.step()
    '''


    f = self.pid.update(self.body.GetWorldCenter(), (15, 15), 1.0*60)
    self.body.ApplyForce(f, self.body.GetWorldCenter())
    t = self.apid.update(self.body.GetAngle(), hurrr.angle.HALF_PI, 1.0*60)
    self.body.ApplyTorque(t)
    self.world.step()
    self.steps+=1
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

    pygame.draw.circle(screen, (204, 102, 102), map(lambda x : int(x), self.window.camera.toScreen((15,15))), int(self.window.camera.scalarToScreen(0.5)))

Game()