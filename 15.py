import time
import math
times = []
times.append(time.clock())
limit = 20

paths = {}
for i in range(limit + 1):
    paths[(i,0)] = 1
    paths[(0,i)] = 1

def findpath(pos):
    if pos[0] < 1 or pos[1] < 1: return
    if (pos[0],pos[1]-1) not in paths: findpath((pos[0],pos[1]-1))
    if (pos[0]-1,pos[1]) not in paths: findpath((pos[0]-1,pos[1]))
    paths[pos] = paths[(pos[0],pos[1]-1)] + paths[(pos[0]-1,pos[1])]

findpath((limit,limit))
print(paths[(limit,limit)])

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])