import time
import math
from functions import tri, unpent, unhexag
times = []
times.append(time.clock())

i = 40756 # want the next one
while True:
    t = tri(i)
    if unpent(t).is_integer() and unhexag(t).is_integer():
        print(t)
        break
    i += 1
times += [time.clock()]
print(times[-1] - times[-2])