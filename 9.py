import time
import math
times = []
times.append(time.clock())

limit = 1000

for a in range(1,limit):
    for b in range(a,limit):
        if a+b+math.sqrt(a*a+b*b) == limit:
            print(a*b*int(math.sqrt(a*a+b*b)))
            break

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])