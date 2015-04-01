import time
import math
from array import array
times = []
times.append(time.clock())
limit = 200

# classic change problem requesting the number of solutions
# this could be rewritten for tail call optimization by passing count value down
# but vanilla python doesn't supprt TCO...

coins = [1, 2, 5, 10, 20, 50, 100, 200]

# naive recursive counting method

def count(value, i):
    if value == 0:
        return 1
    if value < 0:
        return 0
    if i < 0 and value >= 1:
        return 0
    return count(value, i - 1) + count(value - coins[i], i)

print(count(limit, len(coins) - 1))

times.append(time.clock())
print(times[-1] - times[-2])

# dynamic approach with baked in memoization

values = [1] + [0] * limit
for c in coins:
    for x in range(limit - c + 1):
        values[c + x] += values[x]
        
print(values[-1])

times.append(time.clock())
print(times[-1] - times[-2])