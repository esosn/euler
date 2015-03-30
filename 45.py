import time
import math
from functions import tri, unpent, unhexag
times = []
times.append(time.clock())

for i in range(40756, 999999999999):
    t = tri(i)
    p = unpent(t)
    if p != int(p):
        continue
    h = unhexag(t)
    if h != int(h):
        continue
    print(t)
    break
    
times += [time.clock()]
print(times[-1] - times[-2])