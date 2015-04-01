import time
import math
from functions import prime_sieve
times = []
times.append(time.clock())
limit = 600851475143
    
primes = prime_sieve( int(math.sqrt(limit)) )
for p in reversed(primes):
    if limit % p == 0:
        print(p)
        break

times.append(time.clock())
print(times[-1] - times[-2])