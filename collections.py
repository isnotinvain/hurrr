'''
==================================================================
hurrr by Alex Levenson

Custom collections
=================================================================
'''
import heapq

class PriorityQueue(object):
  '''
  A min heap that defers to heapq
  but also maintains a paralell set
  so that __contains__ is O(1)

  Be sure to call heapify() when you modify
  elements inside the heap
  '''
  def __init__(self, elements=None):
    if not elements:
      elements = []
    self.cet = set(elements)
    self.lyst = list(elements)
    if len(self.cet) != len(self.lyst):
      raise ValueError("Elements contains duplicates")
    heapq.heapify(self.lyst)

  def push(self, item):
    self.cet.add(item)
    heapq.heappush(self.lyst, item)

  def pop(self):
    ret = heapq.heappop(self.lyst)
    self.cet.remove(ret)
    return ret

  def heapify(self):
    '''
    IF YOU CHANGE AN ELEMENT IN THIS PQ IN A WAY THAT EFFECTS
    ITS __cmp__, YOU MUST CALL THIS METHOD
    IT'S O(N)
    '''
    heapq.heapify(self.lyst)

  def __len__(self):
    return len(self.cet)

  def __contains__(self, item):
    return item in self.cet