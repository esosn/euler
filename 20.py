import time
import math
times = []
times.append(time.clock())
limit = 100

f = math.factorial(limit)
# eliminate some trailing zeroes
f = f // 10*((limit // 10 + 1)) #5*2
s = str(f)
sum = 0
for c in s:
    sum += int(c)
print(sum)

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])