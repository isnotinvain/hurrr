# hurrr by Alex Levenson

def easeIn(current, target, smooth):
  '''
  Proportionally interpolate current towards
  '''
  return current + (target - current) / smooth