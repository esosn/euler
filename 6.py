import time
import math
from functions import tri
times = []
times.append(time.clock())
limit = 100

sum = 0
for i in range(limit + 1):
    sum += i**2
print(tri(limit)**2 - sum)

times.append(time.clock())
print(times[-1] - times[-2])