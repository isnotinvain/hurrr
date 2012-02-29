# hurrr by Alex Levenson

def constructTriangleFromLine(pt1, pt2):
  '''
  return: a list of points that describe an equilteral triangle around the segment from pt1 --> pt2
  '''

  halfHeightVector = (0.57735 * (pt2[1] - pt1[1]), 0.57735 * (pt2[0] - pt1[0]))
  pt3 = (pt1[0] + halfHeightVector[0], pt1[1] - halfHeightVector[1])
  pt4 = (pt1[0] - halfHeightVector[0], pt1[1] + halfHeightVector[1])
  return (pt2, pt3, pt4)

def polyArea(vertices):
    '''
    return: the area of the polygon described by vertices
    '''
    n = len(vertices)
    A = 0
    p = n - 1
    q = 0
    while q < n:
        A += vertices[p][0] * vertices[q][1] - vertices[q][0] * vertices[p][1]
        p = q
        q += 1
    return A / 2.0