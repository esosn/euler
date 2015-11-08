import time
from functions import tri
times = []
times.append(time.clock())
limit = 1000

# O(n). Naive, but simple and easy to understand

total = 0
for i in range(limit):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)

times.append(time.clock())
print(times[-1] - times[-2])

# O(n) but with coefficient 1/3
# could be further improved with bit shifting instead of modulo

total = -1 # algo calculates answer + 1
fives = limit // 5
for i in range(limit // 3):
    total += 3 * i
    if(i <= fives and i % 3 != 0):
        total += 5 * i
print(total)

times.append(time.clock())
print(times[-1] - times[-2])

# O(1)
# calculate summations directly; they're triangle numbers

total = 3*tri((limit - 1) // 3) + 5*tri((limit - 1) // 5) - 15*tri((limit - 1) // 15)
print(total)

times.append(time.clock())
print(times[-1] - times[-2])