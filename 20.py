import time
import math
times = []
times.append(time.clock())
limit = 100

f = math.factorial(limit)
# eliminate a bunch of zeroes by casting to a string, reversing it,
# casting to an int, which will drop all leading zeroes
# str.replace('0','') is a tiny bit slower on average despite removing all 0s
sum = 0
for c in str(int( str(f)[::-1] )):
    sum += int(c)
print(sum)

times.append(time.clock())
print(times[-1] - times[-2])