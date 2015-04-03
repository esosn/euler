from functions import sumdigits
import time
times = []
times += [time.clock()]
limit = 100

maximum = 0
# using 90s produces the longest numbers, which is where the max sum will be
for a in range(90, limit):
    for b in range(90, limit):
        value = sumdigits(a**b)
        if maximum < value:
            maximum = value
            
print(maximum)

times += [time.clock()]
print(times[-1] - times[-2])