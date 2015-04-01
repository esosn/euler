import time
import math
from collections import deque
from functions import prime_sieve
times = []
times.append(time.clock())
    
primes = prime_sieve(10000)[168:] #first 4 digit prime is #169
pset = set(primes)
pset.discard(1487) # known answer

times.append(time.clock())
print(times[-1] - times[-2])

# naive search
# generates permutations instead of testing them
def permute(p):
    global pset
    pset.discard(p)
    if not (p + 3330 in pset and p + 6660 in pset): return
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
                p1 = int(a + b + c + d)
                if p1 in pset:
                    pset.discard(p1)
                    perms = perms + [p1]
                p2 = int(a + b + d + c)
                if p2 in pset:
                    pset.discard(p2)
                    perms = perms + [p2]
                q.append(c)
                q.append(d)
            q.append(b)
        q.append(a)
    perms.sort()
    values = []
    for i in range(len(perms) - 1):
        for j in range(len(perms) - 1, i, -1):
            diff = perms[j] - perms[i]
            if diff == 3330:
                values = values + [perms[i], perms[j]]
    if len(values) >= 3:
        print(str(values[0]) + str(values[1]) + str(values[3]))
        return True
    return False

#generate sets
for p in primes:
    if not p in pset:
        continue
    if permute(p):
        break
    
times.append(time.clock())
print(times[-1] - times[-2])

# more intelligent search, ~4x faster
pset = set(primes)

def ispermutation(q, r):
    x = sorted(str(q))
    y = sorted(str(r))
    return all([a == b for (a,b) in zip(x, y)])
    
for p in primes[:-2]:
    if p == 1487:
        continue
    p1 = p + 3330
    p2 = p + 6660
    if not (p1 in pset and p2 in pset):
        continue
    if ispermutation(p, p1) and ispermutation(p, p2):
        print(str(p) + str(p1) + str(p2))
        break

times.append(time.clock())
print(times[-1] - times[-2])