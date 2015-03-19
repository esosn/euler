import time
import math
times = []
times.append(time.clock())
limit = 100

def tri(x): return x*(x+1)//2
sum = 0
for i in range(limit + 1): sum += i**2
print(tri(limit)**2 - sum)


times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])