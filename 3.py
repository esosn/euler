import time
import math
times = []
times.append(time.clock())
limit = 600851475143

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
    
primes = primes1( int(math.sqrt(limit)) )
for p in reversed(primes):
    if limit % p == 0:
        print(p)
        break

times.append(time.clock())
print(times[-1] - times[-2])