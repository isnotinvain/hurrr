'''
==================================================================
hurrr by Alex Levenson

A* pathfinding implementation
=================================================================
'''
import collections
import twod

class AStarNode(object):
  def __init__(self, position=None):
    # location in your map, in your coordinates (for your purposes only)
    self.position = position
    # whether this node is actually walkable
    # useful if you want to set a node to invalid
    # due to changing circumstances
    self.walkable = True
    # parent node used for A*
    self.parent = self
    # costs used for A*
    self.G = None
    self.H = None

    self.neighbors = set()

  def getCost(self):
    return self.G + self.H

  def costToGoToNeighbor(self, to):
    '''
    return the cost to walk from self -> to
           where to is a neighbor
           default is Euclidean distance
    '''
    return twod.distance(self.position, to.position)

  def estimateCostToEnd(self, end):
    '''
    return the cost to walk from self -> end
           assuming nothing is in the way
           default is Euclidean distance
    '''
    return twod.distance(self.position, end.position)

  def __eq__(self, other):
      return self is other

  def __ne__(self, other):
      return self is not other

  def __cmp__(self, other):
      return self.getCost() - other.getCost()

  def __repr__(self):
    return str(self.position)

class AStarGridNode(AStarNode):
  def __init__(self, gridSize, position=None):
    AStarNode.__init__(self, position)
    self.gridSize = gridSize

  def estimateCostToEnd(self, end):
    '''
    return the cost to walk from self -> end
           assuming nothing is in the way
           default is chessBoardDistance
    '''
    return twod.chessBoardDistance(self.position, end.position, self.gridSize)

def findPath(startNode, endNode):
  '''
  Runs the A* algorithm
  '''
  openlist = collections.PriorityQueue()
  closedlist = set()

  startNode.G = 0
  startNode.H = startNode.estimateCostToEnd(endNode)

  openlist.push(startNode)

  while len(openlist) > 0 and endNode not in closedlist:
    currentNode = openlist.pop()
    closedlist.add(currentNode)
    for neighbor in currentNode.neighbors:
      if neighbor is currentNode: continue
      if neighbor in closedlist: continue
      if not neighbor.walkable: continue

      tentativeG = currentNode.G + currentNode.costToGoToNeighbor(neighbor)

      if neighbor not in openlist:
        neighbor.H = neighbor.estimateCostToEnd(endNode)
        neighbor.G = tentativeG
        neighbor.parent = currentNode
        openlist.push(neighbor)
      elif tentativeG < neighbor.G:
        neighbor.parent = currentNode
        neighbor.G = tentativeG
        openlist.heapify()

  if endNode in closedlist:
    path = []
    finger = endNode
    while finger is not startNode:
      path.append(finger)
      finger = finger.parent
    path.reverse()
    return path
  else:
    return None