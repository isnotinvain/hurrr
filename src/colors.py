'''
==================================================================
hurrr by Alex Levenson

Some color constants
=================================================================
'''
import lang.Enum

# standard color scheme
STANDARD = lang.Enum( \
  WHITE=(255, 255, 255), \
  BLACK=(0, 0, 0), \
  RED=(255, 0, 0), \
  GREEN=(0, 255, 0), \
  BLUE=(0, 0, 255), \
  YELLOW=(255, 255, 0), \
  ORANGE=(255, 128, 0), \
  PURPLE=(128, 0, 128), \
  TAN=(210,180,140)
)

# LCARS color scheme
LCARS = lang.Enum( \
  WHITE=(255, 255, 255), \
  BLACK=(0, 0, 0), \
  RED=(204, 102, 102), \
  GREEN=(102, 204, 102 ), \
  BLUE=(153, 153, 204), \
  YELLOW=(255, 153, 102), \
  ORANGE=(255, 153, 0), \
  PURPLE=(204, 102, 153), \
  TAN=(255, 204, 153)
)