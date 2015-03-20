import time
import math
times = []
times.append(time.clock())

f1 = 1
f2 = 1
f3 = 2

term = 3
while len(str(f3)) < 1000:
    f1 = f2
    f2 = f3
    f3 = f1 + f2
    term += 1
print(term)

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])