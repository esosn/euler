import math
import time
import re
times = []
times.append(time.clock())

def tri(n): return n*(n+1)//2
def untri(n): return int((math.sqrt(1+8*n)-1) // 2)

problem = '067'
fo = open('p'+str(problem)+'_triangle.txt')
data = [int(n) for n in re.split(r'\s*',fo.read()) if n != '']
fo.close()

# # known test data, answer = 23
# data = [3, \
# 7, 4, \
# 2, 4, 6, \
# 8, 5, 9, 3]

# first index in each row is a square number
# 0 based indexing means that arraylength = tri(depth)
limit = untri(len(data))
goals = range(len(data)-limit, len(data))
seen = {0:data[0]}

# O(n) bfs using priority queue to find min path of negative weights
def traverse(depth):
    global limit,seen,goals
    if depth > limit: return
    pmin = tri(depth-2)
    pmax = tri(depth-1)
    for i in range(tri(depth-1),tri(depth)):
        p0 = i-depth
        p1 = p0+1
        parentcost = 0
        if p0 >= pmin and p0 < pmax:
            pcost = seen[p0] if p0 in seen else 0
            parentcost = min(-1 * data[p0], pcost, parentcost)
        if p1 >= pmin and p1 < pmax:
            pcost = seen[p1] if p1 in seen else 0
            parentcost = min(-1 * data[p1], pcost, parentcost)
        cost = -1 * data[i] + parentcost
        if i in seen: seen[i] = min(cost, seen[i])
        else: seen[i] = cost
    traverse(depth+1)

traverse(2)
minimum = 0
for g in goals:
    minimum = min(seen[g],minimum)
print(minimum*-1)

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])