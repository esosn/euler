# handy functions

import time
import math
times = []
times.append(time.clock())
limit = 1

times.append(time.clock())
print(times[-1] - times[-2])

def countdivisors(n):
    return sum(2 for i in range(1, int(math.sqrt(n)) + 1) if not n % i)

# stein's algorithm
def gcd(u, v):
    if u == 0:
        if v == 0:
            return 0
        return v
    elif v == 0:
        return x
    if u == v:
        return u
    k = 0
    while u != v and u > 0:
        if u % 2 == 0:
            u = u // 2
            if v % 2 == 0:
                v = v // 2
                k += 1
        elif v % 2 == 0:
            v = v // 2
        else:
            if u >= v:
                u = (u - v) // 2
            else:
                newv = u
                u = (v - u) // 2
                v = newv
    return v * 2 ** k

def getdivisors(n):
    divs = set()
    for x in range(1, int(math.sqrt(n)) + 1):
        dm = divmod(n, x)
        if not dm[1]:
            divs.add(x)
            if dm[0] != n: divs.add(dm[0])
    return divs

def is19pandigital(s):
    seen = set()
    for c in s:
        if c == '0' or c in seen:
            return False
        seen.add(c)
    return True

def ispalindrome(n):
    x = str(n)
    return x == x[::-1]

# sundaram implementation originally by Robert William Hanks
# http://stackoverflow.com/a/3035188/1046207
# adapted for python 3
def sundaram(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n // 2)
    primes = set([1] * (n // 2))
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i*i // 2::i] = [False] * ((n - i*i - 1) // (2*i) + 1)
    return [2] + [2*i + 1 for i in range(1, n // 2) if sieve[i]]
    
def tri(n):
    return n * (n + 1) // 2

def untri(n):
    return (math.sqrt(1 + 8 * n) - 1) / 2 