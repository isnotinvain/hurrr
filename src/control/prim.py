'''
==================================================================
hurrr by Alex Levenson

Utilities for controlling bodies in an asteroids style
2D environment (no gravity, top down) at the primitive level
(physical movement in space)
=================================================================
'''
from .. import angle
from .. import twod

def torqueToRotate(radians, momentInertia, currentVelocity, time):
  '''
  return the torque needed to rotate a (potentially) already rotating body
  radians: how much to rotate the body from its current angle
  momentInertia: the MOI of the body
  currentVelocity: current angular velocity of the body
  time: how many seconds should it take to rotate
  '''
  velocityNeeded = radians / time
  accelerationNeeded = (velocityNeeded - currentVelocity) / time
  torqueNeeded = momentInertia * accelerationNeeded
  return torqueNeeded

def torqueToSetVelocity(currentVelocity, targetVelocity, momentInertia, time):
  '''
  return the torque needed to set the angular velocity of a
         (potentially) already rotating body
  currentVelocity: current angular velocity of the body
  targetVelocity: angular velocity you want the body to have
  momentInertia: the MOI of the body
  time: how many seconds should it take to change the velocity to targetVelocity
  '''
  return ((targetVelocity - currentVelocity) / time) * momentInertia

def forceToMove(distance, mass, currentVelocity, time):
  '''
  return the force needed to move a (potentially) already moving
         body a distance
  distance: how far to move the body
  mass: mass of the body
  currentVelocity: the current velocity of the body
  time: how long should it take to move the body
  '''
  fx = torqueToRotate(distance[0], mass, currentVelocity[0], time)
  fy = torqueToRotate(distance[1], mass, currentVelocity[1], time)
  return (fx, fy)

def forceToSetVelocity(currentVelocity, targetVelocity, mass, time):
  '''
  return the force needed to set the velocity of a (potentially)
         already moving body
  currentVelocity: current velocity of the body
  targetVelcoty: velocity you want the body to have
  mass: mass of the body
  time: how many seconds it should take to change the velocity to targetVelocity
  '''
  fx = torqueToSetAngularVelocity(currentVelocity[0],targetVelocity[0], mass, time)
  fy = torqueToSetAngularVelocity(currentVelocity[0],targetVelocity[0], mass, time)
  return (fx, fy)

class PIDController(object):
  '''
  Calculates the force / torque / voltage / power level
  needed to controll a body using Proportional-Integral-Derivative Control
  and maintains the state needed to do so
  '''
  def __init__(self, kp, kd, ki, kiDamp):
    '''
    kp: proportional control modifier
    kd: derivative control modifier
    ki: integral control modifier
    kiDamp: integral control memmory modifier
            (should be <= 1.0)
            1.0 makes this PID an elephant: it never forgets
            The closer to 0.0 it is the less old errors count
    '''
    self.kp = kp
    self.kd = kd
    self.ki = ki
    self.kiDamp = kiDamp
    self.reset()

  def calcError(self, current, desired):
    '''
    Override this for non-linear spaces
    '''
    return desired - current

  def update(self, current, desired, deltaT):
    '''
    return the force / torque / voltage / power level to apply
    '''
    error = self.calcError(current, desired)
    derivative = (error - self.previousError)
    self.previousError = error
    self.integral += self.kiDamp * error
    return self.kp * error + self.kd * derivative + self.ki * self.integral

  def reset(self):
    '''
    Reset this controller's state
    Use in scenarios where the previous errors are no longer valid
    Such as:
      the goal has changed / moved (by a lot)
      the agent has been magically transported to a new location
      the agent has been bumped into really hard / spun around etc.
    '''
    self.previousError = 0.0
    self.integral = 0.0

class TwodPIDController(object):
  def __init__(self, pidx, pidy):
    self.pidx = pidx
    self.pidy = pidy

  def update(self, current, desired, deltaT):
    return self.pidx.update(current[0], desired[0], deltaT), self.pidy.update(current[1], desired[1], deltaT)

  def reset(self):
    self.pidx.reset()
    self.pidy.reset()

class RotationalPIDController(PIDController):
  '''
  PID controller for controlling angles / rotating agents
  Uses shortestTurn for determining error
  '''
  def calcError(self, current, desired):
    return angle.shortestTurn(current, desired)
