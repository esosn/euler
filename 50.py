import time
import math
from functions import prime_sieve
times = []
times.append(time.clock())

limit = 1000000
primes = prime_sieve(limit)
pset = set(primes)

# search with a sliding window that shrinks in size

maxi = len(primes)
start = sum(primes[:-1])
stop = False
if start in pset:
    print(start)
else:  
    for i in range(maxi - 2, 2, -1):
        x = start
        for j in range(maxi - i):
            x = x - primes[j] + primes[j + i + 1]
            if x > limit:
                break
            if x in pset:
                print(x)
                stop = True
                break
        if stop:
            break
        start -= primes[i]
        if start in pset:
            print(start)
            break
        
times.append(time.clock())
print(times[-1] - times[-2])