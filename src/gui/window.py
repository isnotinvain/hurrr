import sys
import pygame
from pygame.locals import QUIT

class Window(object):
  '''
  A really simple pygame window w/ main loop
  You can only create one of these!
  More specifically, you can create any number of Window objects,
  but calling run() more than once (or once on more than one Window)
  will cause all kinds of problems. run() creates / opens the main pygame window
  '''
  def __init__(self, size=None, fps=60, bgColor=(0,0,0), updateFunction=lambda: None, drawFunction=lambda x: None):
    '''
    size: window size, defaults to 75% of full screen
    fps: target frames per second: this will effect BOTH rate of update and rate of drawing
    bgColor: what color to use to clear the screen
    updateFunction: called once per loop, this is where the 'work' of you app goes
                    updateFunction should return False if it wants to cose the window
    drawFunction: called after  updateFunction with the screen as a parameter,
                  you should draw everything onto the screen here
    '''
    self.fps=fps
    self.bgColor=bgColor
    self.updateFunction = updateFunction
    self.drawFunction = drawFunction
    self.size = size

  def run(self):
    '''
    Initializes pygame, opens the main pygame window, and begins the app's main loop
    See notes in docs above
    '''
    pygame.init()
    pygame.display.init()
    if not self.size:
      size = pygame.display.list_modes()[0]
      size = map(lambda x : int(x * 0.75), size)
    self.screen = pygame.display.set_mode(size)
    pygame.font_instance = pygame.font.Font(None, 20)

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

      if not self.updateFunction():
        # bye bye! Hope you had fun!
        break

      # clear the display
      self.screen.fill(self.bgColor)

      self.drawFunction(self.screen)

      # blit to the screen
      pygame.display.flip()

      # try to stay at specified FPS
      self.clock.tick(self.fps)
