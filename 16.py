import time
import math
times = []
times.append(time.clock())
limit = 1000

num = str(2**limit)
value = 0
for s in num: value += int(s)
print('%d' % value)

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])

