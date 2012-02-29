# hurrr by Alex Levenson

class Enum(object):
  '''
  A simple Enum implementation

  useage:
    verbs = Enum.new("HURPING", "SKURPING", "DURPING")
    currentState = verbs.HURPING
    if currentState == verbs.HURPING:
      print "hurping!"

  This is based on an answer to a stack overflow question written by:
  http://stackoverflow.com/users/7980/alec-thomas

  I couldn't find a way to contact him so: thanks Alec!
  '''

  @classmethod
  def new(cls, *seq, **named):
    if len(named) > 0:
      raise ValueError("Keyword arguments not supported")
    if len(seq) != len(set(seq)):
      raise ValueError("Duplicate keys in enum:" + str(seq))
    enums = dict(zip(seq, xrange(len(seq))))
    return type('Enum', (cls,), enums)