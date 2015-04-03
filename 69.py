from functions import prime_sieve, primefactors
import time
import math
times = []
times += [time.clock()]
limit = 1000000

primes = prime_sieve(int(math.sqrt(limit)))
maximum = 2
maxn = 2

# phi(2n) = {2phi(n) if n is even; phi(n) if odd}
# phi(nm) = phi(n) * phi(m) if n, m are coprime
# maxn will be even but eventually need to calculate some odd values
# searching the range by calculating totients takes about a minute...

# totients = {2:1}
# for n in range(3, limit):
#     if not n % 2:
#         m = n // 2
#         value = totients[m]
#         if not m % 2:
#             value *= 2 
#     else:
#         value = totient(n, primes)
#     totients[n] = value
#     x = n / value
#     if x > maximum:
#         maximum = x
#         maxn = n

# ... but is a waste of time. some alegbra reveals:
# n/phi(n) = pi(p/(p-1)) for p|n
# which is maximized by pi(p) for p < n

value = 1
maxp = 2
for p in primes:
    value *= p
    if value > limit:
        value = value // p
        break
    maxp = p
    if value == limit:
        break

print(value)
times += [time.clock()]
print(times[-1] - times[-2])