import time
import math
from collections import deque
from functions import prime_sieve
times = []
times += [time.clock()]

limit = 10**6
    
primes = prime_sieve(limit)
pset = set(primes)

times += [time.clock()]
print(times[-1] - times[-2])

def permute(p):
    s = str(p)
    number = 1
    for i in range(len(s) - 1):
        s = s[-1] + s[:-1]
        p0 = int(s)
        if not p0 in pset:
            return 0
        elif p0 != p and p0 in pset:
            number += 1
            pset.discard(p0)
    pset.discard(p)
    return number
    
pcount = 0
for p in primes:
    if p in pset:
        pcount += permute(p)
print(pcount)
        
times += [time.clock()]
print(times[-1] - times[-2])