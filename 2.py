import time
import math
times = []
times.append(time.clock())
limit = 4000000

f0 = 1
f1 = 2
summation = 0
while f1 < limit:
    if f1 % 2 == 0: summation += f1
    f2 = f0 + f1
    f0 = f1
    f1 = f2
print(summation)

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])