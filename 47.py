import time
import math
from functions import prime_sieve
from array import array
times = []
times.append(time.clock())

# brute force, generating a list of 4-factors and checking for runs
# or composites and checking the factors was really, really slow :(

runsize = 4
limit = 1000000
primes = prime_sieve(1000)

def haspfacts(index):
    for i in range(runsize):
        x = index + i
        count = 0
        for p in primes:
            if x % p == 0:
                count += 1
                if count == runsize:
                    break
        if count < runsize:
            return False
    print(index)
    return True

for i in range(210, limit): # 210 = 2*3*5*7
    if haspfacts(i):
        break
        
times.append(time.clock())
print(times[-1] - times[-2])

# a modified sieve of eratosthenes is a much better approach

factors = [0] * limit
for i in range(2, limit):
    if factors[i] == runsize:
       if factors[i + 1] == runsize and \
       factors[i + 2] == runsize and factors[i + 3] == runsize:
          print(i)
          break
    else:
       if factors[i] == 0:
          for j in range(2, math.floor(limit / i)):
              factors[i * j] += 1
              
times.append(time.clock())
print(times[-1] - times[-2])