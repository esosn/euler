import time
import math
times = []
times.append(time.clock())
limit = 500

def tri(n):
    return n * (n + 1) // 2

def countdivs(n):
    return sum(2 for i in range(1, int(math.sqrt(n)) + 1) if not n % i)

t = tri(2 * limit)
n = 2 * limit

# just brute force count tri numbers until one is found
notfound = True
while True:
    if countdivs(t) > limit:
        print(t)
        break
    n += 1
    t += n

times.append(time.clock())
print(times[-1] - times[-2])