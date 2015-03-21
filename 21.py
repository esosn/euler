import time
import math
times = []
times.append(time.clock())
limit = 10000

def sumfactors(n):
    factors = {1}
    summation = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if i not in factors:
            if n % i == 0:
                factors.add(i)
                summation += i
                j = n//i
                if j not in factors:
                    factors.add(j)
                    summation += j
    return summation

# naive solution, polynomial time
total = 0 
seen = {}
for i in range(2, limit):
    j = sumfactors(i)
    if j > i and j < limit and j < 1.5 * i:
        seen[j] = i
    elif i in seen and seen[i] == j:
        total += i + j
print(total)

times.append(time.clock())
print(times[-1] - times[-2])