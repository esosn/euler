import time
import math
times = []
times.append(time.clock())
limit = 100

# memoize factorials
facts = {0:1}
    
total = 0
for n in range(1, limit + 1):
    if n in facts:
        nfact = facts[n]
    else:
        nfact = math.factorial(n)
        facts[n] = nfact
    for r in range(1, n + 1):
        if r in facts:
            rfact = facts[r]
        else:
            rfact = math.factorial(r)
            facts[r] = rfact
        nr = n - r
        if nr in facts:
            nrfact = facts[nr]
        else:
            nrfact = math.factorial(nr)
            facts[nr] = nrfact
        if nfact / (rfact * nrfact) > 1000000:
            total += 1
print(total)
    
times.append(time.clock())
print(times[-1] - times[-2])