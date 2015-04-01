import time
import math
from functions import prime_sieve
times = []
times.append(time.clock())
limit = 10000

# simple search is quite fast

primes = prime_sieve(limit)
pset = set(primes)
composites = set(x for x in range(9, limit, 2)) - pset
squares = [2*x*x for x in range(1, int(math.sqrt(limit)))]

for s in squares:
    for p in primes:
        composites.discard(p + s)

print(sorted(composites)[0])

times.append(time.clock())
print(times[-1] - times[-2])