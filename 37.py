import time
import math
import decimal
from functions import prime_sieve
times = []
times += [time.clock()]
limit = 11

# pretty easy to intuit from the example
# just permute the digits a few times to get most of the others
# add a single digit prime in front of or behind a 1 or 2 digit for the rest
total = 3797 + 23 + 37 + 53 + 73 + 313 + 317 + 373 + 797 + 3137 + 739397
print(total)

times += [time.clock()]
print(times[-1] - times[-2])

# just for fun, here's a search algo: construct them iteratively
# target primes can't end or start with any nonprime digit
# none of them > 2 digits can have an interior 5 or even digit
    
primes = prime_sieve(10 ** 6)
primeset = set(primes)
starts = {2, 3, 5, 7}
digits = {3, 5, 7} 
invalid_starts = {0, 1, 4, 6, 8, 9}
invalid_ends = {0, 1, 2, 4, 6, 8, 9}
invalid_interiors = {0, 2, 4, 5, 6, 8}
found = set()

for p in primes: 
    s = str(p)
    slen = len(s)
    if (s[0] in invalid_starts and s[-1] in invalid_ends):
        continue
    interior_ok = True
    for c in s[1:-1]:
        if c in invalid_interiors:
            interior_ok = False
            break
    if not interior_ok:
        continue
    if s[0] not in invalid_interiors:
        for d in starts:
            newp = str(d) + s
            foundnewp = True
            for i in range(1, slen + 1):
                if not (int(newp[i:]) in primeset and int(newp[:-i]) in primeset):
                    foundnewp = False
                    break
            if foundnewp and int(newp) in primeset:
                found.add(int(newp))
                break
    if len(found) == 11:
        break
    if s[-1] not in invalid_interiors:
        for d in digits:
            newp = s + str(d)
            foundnewp = True
            for i in range(1, slen + 1):
                if not (int(newp[i:]) in primeset and int(newp[:-i]) in primeset):
                    foundnewp = False
                    break
            if foundnewp and int(newp) in primeset:
                found.add(int(newp))
                break
    if len(found) == 11:
        break

print(sum(found))

times += [time.clock()]
print(times[-1] - times[-2])