import time
from functions import islychrel
times = []
times.append(time.clock())
limit = 10000

count = 0
for i in range(10, limit):
    if islychrel(i, 0, 50):
        count += 1
        
print(count)

times.append(time.clock())
print(times[-1] - times[-2])