'''
==================================================================
hurrr by Alex Levenson

A really simple pygame window w/ main loop
=================================================================
'''
import sys
import pygame
from pygame.locals import QUIT
from camera import Camera
class Window(object):
  '''
  A really simple pygame window w/ main loop
  You can only create one of these!
  More specifically, you can create any number of Window objects,
  but calling run() more than once (or once on more than one Window)
  will cause all kinds of problems. run() creates / opens the main pygame window
  '''
  def __init__(self, \
              size=None, \
              fps=60, \
              bgColor=(0,0,0), \
              updateFunc=lambda: None, \
              drawFunc=lambda x: None, \
              screenToWorldRatio=1.0):
    '''
    size: window size, defaults to 75% of full screen
    fps: target frames per second: this will effect BOTH rate of update and rate of drawing
    bgColor: what color to use to clear the screen
    updateFunc: called once per loop, this is where the 'work' of you app goes
                    updateFunc should return False if it wants to cose the window
    drawFunc: called after  updateFunc with the screen as a parameter,
                  you should draw everything onto the screen here
    '''
    self.fps=fps
    self.bgColor=bgColor
    self.updateFunc = updateFunc
    self.drawFunc = drawFunc
    self.size = size
    self.screenToWorldRatio = screenToWorldRatio

  def run(self, setupWindow=lambda w: None):
    '''
    Initializes pygame, opens the main pygame window,
    calls setupWindow(self)
    and begins the app's main loop
    See notes in docs above
    '''
    pygame.init()
    pygame.display.init()
    if not self.size:
      self.size = pygame.display.list_modes()[0]
      self.size = map(lambda x : int(x * 0.75), self.size)
    self.screen = pygame.display.set_mode(self.size)
    self.camera = Camera(self.screenToWorldRatio, True, self.size[1])
    pygame.font_instance = pygame.font.Font(None, 20)
    self.clock = pygame.time.Clock()

    setupWindow(self)

    self.running = True
    while self.running:
      # handle events
      for event in pygame.event.get():
        if event.type == QUIT:
          self.running = False
          break

      if not self.running:
        # bye bye! Hope you had fun!
        break

      if not self.updateFunc():
        # bye bye! Hope you had fun!
        break

      # clear the display
      self.screen.fill(self.bgColor)

      self.drawFunc(self.screen)

      # blit to the screen
      pygame.display.flip()

      # try to stay at specified FPS
      self.clock.tick(self.fps)
