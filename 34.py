import time
import math
times = []
times.append(time.clock())

facts = {x:math.factorial(x) for x in range(10)}

def getfsum(n):
    s = str(n)
    total = 0
    for c in s:
        total += facts[int(c)]
    return total

summation = 0
for i in range(10, 1000000):
    if getfsum(i) == i:
        summation += i

print(summation)

times.append(time.clock())
print(times[-1] - times[-2])