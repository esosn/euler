import time
import math
times = []
times.append(time.clock())
limit = 20



paths = {}
for i in range(limit + 1):
    paths[(i,0)] = 1
    paths[(0,i)] = 1

# by searching

def findpath(pos):
    if pos[0] < 1 or pos[1] < 1: return
    if (pos[0], pos[1] - 1) not in paths: findpath((pos[0], pos[1] - 1))
    if (pos[0] - 1, pos[1]) not in paths: findpath((pos[0] -1 , pos[1]))
    paths[pos] = paths[(pos[0], pos[1] - 1)] + paths[(pos[0] - 1, pos[1])]

findpath((limit, limit))
print(paths[(limit, limit)])

times.append(time.clock())
print(times[-1] - times[-2])

# bisecting along the orthogonal diagonal produces pascal's triangle
# middle cell in row limit will have number of paths
# middle(row n) = sum(row n/2)
# sum(row n) = (n, k-1) x (n+1 - k) / k

curcell = 1
for i in range(1, limit + 1):
    curcell *= (limit * 2 + 1 - i) / i
print(curcell)

times.append(time.clock())
print(times[-1] - times[-2])

# by direct computation: number of paths = (n+n)! / (n!*n!)
print(math.factorial(limit * 2) // (math.factorial(limit) ** 2))

times.append(time.clock())
print(times[-1] - times[-2])