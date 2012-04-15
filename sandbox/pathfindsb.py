from hurrr.pathfind import *

rows = []
for x in xrange(50):
  rows.append([])
  for y in xrange(50):
    rows[x].append(AStarGridNode(10,position=(x*10,y*10)))
    if x == 3 and y < 10:
      rows[x][y].walkable = False

for x in xrange(50):
  for y in xrange(50):
    for i in [-1, 0, 1]:
      for j in [-1, 0, 1]:
        if i==0 and j==0: continue
        if x+i < 0 or x+i >= len(rows) or y+j < 0 or y+j >= len(rows[x]): continue
        rows[x][y].neighbors.add(rows[x+i][y+j])

rows[48][0].walkable = False
rows[48][1].walkable = False
start = rows[0][0]
end = rows[49][0]

path = findPath(start, end)
print path
out = ""
for y in xrange(50):
  for x in xrange(50):
    if rows[x][y] == start:
      out+="s"
    elif rows[x][y] == end:
      out+="e"
    elif rows[x][y] in path:
      out+="p"
    elif rows[x][y].walkable:
      out+="."
    else:
      out+="x"
  out+="\n"
print out