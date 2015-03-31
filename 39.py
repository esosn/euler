import time
import math
from array import array
times = []
times.append(time.clock())
limit = 1000

# dickson's method for finding pythagorean triples
# find positive ints r, s, t; r2 = 2st
# a, b, c = r + s, r + t, r + s + t

perimeters = array('i', (0 for x in range(limit + 1)))
for r in range(1, limit // 4): # limit >= 3r + 2s + 2t; r2 = 2st
    r2 = r * r
    st = r2 / 2
    for s in range(1, int(st // 2)):
        t = st / s
        if not t.is_integer():
            continue
        p = int(r + s + r + t + r + s + t)
        if p <= limit:
            perimeters[p] = perimeters[p] + 1
            
maxp = 0
maxcount = 0
for p in range(limit + 1):
    if perimeters[p] > maxcount:
        maxcount = perimeters[p]
        maxp = p
        
print(int(maxp))

times.append(time.clock())
print(times[-1] - times[-2])