import time
import math
from collections import deque
times = []
times.append(time.clock())

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
primes = primes1(10000)[168:] #first 4 digit prime is #169
pset = set(primes)

def permute(p):
    global pset
    pset.discard(p)
    if not p + 3330 in pset: return
    perms = [p]
    s = str(p)
    q = deque(s)
    for i in range(4):
        a = q.popleft()
        for j in range(3):
            b = q.popleft()
            for k in range(2):
                c = q.popleft()
                d = q.popleft()
                p1 = int(a+b+c+d)
                if p1 in pset:
                    pset.discard(p1)
                    perms = perms + [p1]
                p2 = int(a+b+d+c)
                if p2 in pset:
                    pset.discard(p2)
                    perms = perms + [p2]
                q.append(c)
                q.append(d)
            q.append(b)
        q.append(a)
    perms.sort()
    values = []
    for i in range(len(perms)-1):
        for j in range(len(perms)-1,i,-1):
            diff = perms[j]-perms[i]
            if diff == 3330:
                values = values + [perms[i],perms[j]]
    if len(values) >= 3:
        print(str(values[0])+str(values[1])+str(values[3]))

#generate sets
for p in primes:
    if not p in pset: continue
    permute(p)

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])