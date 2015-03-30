import time
import math
from functions import pent, unpent
times = []
times.append(time.clock())

# dfs guaranteed to find min diff first
# naive O(n2) search algorithm
    
ps = set()
found = False
i = 1
while not found:
    psum = pent(i)
    for p1 in ps:
        p0 = psum - p1
        if not p0 in ps:
            continue
        pdiff = p1 - p0
        if not pdiff in ps:
            continue
        print(pdiff)
        found = True
        break
    ps.add(psum)
    i += 1
        
times += [time.clock()]
print(times[-1] - times[-2])