import time
import math
from functions import prime_sieve
times = []
times.append(time.clock())
limit = 10001

# nth prime bounded by n ln n + n ln ln n
bound = int( limit * math.log(limit) + limit * math.log(math.log(limit)) ) + 1
primes = prime_sieve(bound)
print(primes[limit - 1])

times.append(time.clock())
print(times[-1] - times[-2])