import time
import math
from collections import deque
times = []
times += [time.clock()]

limit = 10**6

# sundaram implementation originally by Robert William Hanks
# http://stackoverflow.com/a/3035188/1046207
# adapted for python 3
def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    primes = set([1] * (n//2))
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]
    
primes = primes1(limit)
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