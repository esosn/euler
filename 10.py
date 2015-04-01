import time
from functions import prime_sieve
times = []
times.append(time.clock())
limit = 2000000

print(sum(prime_sieve(limit)))

times.append(time.clock())
print(times[-1] - times[-2])