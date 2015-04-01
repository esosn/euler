import time
import math
times = []
times.append(time.clock())
limit = 1000

# brute force is really easy on this one
# done more naturally with str slicing, but mod is a little faster here

print((10405071317 + sum(i**i for i in range(11, limit))) % 10**10)

times.append(time.clock())
print(times[-1] - times[-2])