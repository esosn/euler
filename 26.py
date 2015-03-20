import time
import math
times = []
times.append(time.clock())
limit = 1000

largest = 0
d = 1
for a in range(2,limit):
    if a % 2 == 0 or a % 5 == 0: continue
    k = 1
    while (10**k) % a != 1: k += 1
    if k > largest:
        d = a
        largest = k
print(d)

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])