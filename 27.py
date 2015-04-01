import time
import math
import miller_rabin
from functions import prime_sieve
times = []
times.append(time.clock())
limit = 1000

plist = prime_sieve(limit)
        
def countruns(a, b):
    global maxrun, maxa ,maxb
    n = 1 # b is always prime
    count = 1
    value = n * n + n * a + b
    while miller_rabin.isprime(value):
        count += 1
        n += 1
        value = n * n + n * a + b
    if count > maxrun:
        maxrun = count
        maxa = a
        maxb = b
    
maxa = 0
maxb = 0
maxrun = 0
for b in plist: # start with n=0, so b must be prime
    for a in range(limit):
        countruns(a, b)
        countruns(-a, b)
        # no -b because negatives aren't prime
        # could speed this up by combining the count loop for a and -a
        
print(maxa * maxb)
    
times.append(time.clock())
print(times[-1] - times[-2])