'''
==================================================================
hurrr by Alex Levenson

A 2D physics simulator powered by Box2D

NOTE:
method bodiesAtPoint modified from the Elements source (formerly: http://elements.linuxuser.at)
Can't seem to find the Elements project online though, so I don't know how to properly attribute
=================================================================
'''
import Box2D as box2d
from .. import lang

class Simulator(object):
  """
  Encapsulates the Box2D simulation and
  provides useful physics related functions
  """
  def __init__(self, dimensions=((0,0),(100,100)), \
                     gravity=(0,0), \
                     velocityIterations=20, \
                     positionIterations=20, \
                     timeStep=1.0/60):
    # set up box2D
    worldAABB = box2d.b2AABB()
    lower, upper = dimensions
    worldAABB.lowerBound.Set(*lower)
    worldAABB.upperBound.Set(*upper)
    self.world = box2d.b2World(worldAABB, gravity, True) #doSleep=True

    self.dimensions = dimensions
    self.gravity = gravity
    self.velocityIterations = velocityIterations
    self.positionIterations = positionIterations
    self.timeStep = timeStep
    self.contactListener = ContactListener()
    self.world.SetContactListener(self.contactListener)

  def step(self):
    '''
    Advance the simulation one timestep
    '''
    self.world.Step(self.timeStep, self.velocityIterations, self.positionIterations)

  def addBody(self, pos, parent=None, sleepFlag=True, isBullet=False, linearDamping=0.01, angularDamping=0.01):
    '''
    Add a body to the simulation at pos
    Optionaly set parent in order to get from this body -> the game object it represents
    '''
    bodyDef = box2d.b2BodyDef()
    bodyDef.position.Set(*pos)
    bodyDef.sleepFlag = sleepFlag
    bodyDef.isBullet = isBullet
    bodyDef.linearDamping = linearDamping
    bodyDef.angularDamping = angularDamping
    body = self.world.CreateBody(bodyDef)
    body.userData = {'parent':parent, 'id': id(body)}
    return body

class ContactListener(box2d.b2ContactListener):
  CONTACT_TYPES = lang.Enum.new("ADD", "PERSIST", "REMOVE", "RESULT")
  def __init__(self):
    box2d.b2ContactListener.__init__(self)
    self.callbacks = {}

  def connect(self, body, callback):
    '''
    Connects a callback to a body
    Callback should be a function that accepts two parameters: CONTACT_TYPES type, TUPLE point
    '''
    self.callbacks[body.GetUserData()['id']] = cb

  def disconnect(self, body):
    '''
    Remove a callback from a body
    '''
    if self.callbacks[body.GetUserData()['id']]:
      del self.callbacks[body.GetUserData()['id']]

  def Add(self, point):
    b1 = point.shape1.GetBody().GetUserData()['id']
    b2 = point.shape2.GetBody().GetUserData()['id']

    if self.callbacks.has_key(b1):
      self.callbacks[b1](CONTACT_TYPES.ADD, point)
    if self.callbacks.has_key(b2):
      self.callbacks[b2](CONTACT_TYPES.ADD, point)

  def Persist(self, point):
    b1 = point.shape1.GetBody().GetUserData()['id']
    b2 = point.shape2.GetBody().GetUserData()['id']

    if self.callbacks.has_key(b1):
      self.callbacks[b1](CONTACT_TYPES.PERSIST, point)
    if self.callbacks.has_key(b2):
      self.callbacks[b2](CONTACT_TYPES.PERSIST, point)

  def Remove(self, point):
    b1 = point.shape1.GetBody().GetUserData()['id']
    b2 = point.shape2.GetBody().GetUserData()['id']

    if self.callbacks.has_key(b1):
      self.callbacks[b1](CONTACT_TYPES.REMOVE, point)
    if self.callbacks.has_key(b2):
      self.callbacks[b2](CONTACT_TYPES.REMOVE, point)

  def Result(self, point):
    b1 = point.shape1.GetBody().GetUserData()['id']
    b2 = point.shape2.GetBody().GetUserData()['id']

    if self.callbacks.has_key(b1):
      self.callbacks[b1](CONTACT_TYPES.RESULT, point)
    if self.callbacks.has_key(b2):
      self.callbacks[b2](CONTACT_TYPES.RESULT, point)
