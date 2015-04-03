# handy functions
import time
import math
from collections import deque

# counts all divisors
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

# gets proper divisors
def getdivisors(n):
    divs = set()
    for x in range(1, int(math.sqrt(n)) + 1):
        dm = divmod(n, x)
        if not dm[1]:
            divs.add(x)
            if dm[0] != n: divs.add(dm[0])
    return divs

def hept(n):
    x = int(n)
    return x * (5 * x - 3) // 2

def hexag(n):
    x = int(n)
    return x * (2 * x - 1)

def islychrel(n, depth, maxdepth):
    if depth >= maxdepth:
        return True
    x = n + int(str(str(n)[::-1]))
    if ispalindrome(x):
        return False
    return islychrel(x, depth + 1, maxdepth)
    
def ispandigital(x, n = 9, incl_zero = False):
    s = str(x)
    maxlen = n if not incl_zero else n + 1
    if len(s) != maxlen:
        return False
    seen = set()
    for c in s:
        if (not incl_zero and c == '0') or c in seen or int(c) > n:
            return False
        seen.add(c)
    return True

def ispalindrome(n):
    x = str(n)
    return x == x[::-1]

def ncr(n, r):
    nfact = math.factorial(n)
    rfact = math.factorial(r)
    return nfact / (rfact * math.factorial(n - r))

def octag(n):
    x = int(n)
    return x * (3 * x - 2)

def pent(n):
    x = int(n)
    return n * (3 * n - 1) // 2

# callback needs to be defined with a *args or **args param at the end
# def my_callback(*args):
#     cb_args = args[-1]
def permute(s, dq, depth, maxdepth, callback, cb_args):
    if depth >= maxdepth:
        callback(s, dq, depth, maxdepth, cb_args)
        return
    for i in range(len(dq)):
        x = str(dq.popleft())
        permute(str(s) + x, dq, depth + 1, maxdepth, callback, cb_args)
        dq.append(x)

# sieve implementation originally by Robert William Hanks
# http://stackoverflow.com/a/3035188/1046207
# adapted for python 3
def prime_sieve(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = [True] * (n // 3)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3*i + 1 | 1
            sieve[k*k // 3::2*k] = [False] * ((n // 6 - k*k // 6 - 1) // k + 1)
            sieve[k*(k - 2*(i & 1) + 4) //3::2*k] = \
            [False] * ((n // 6 - k*(k - 2*(i & 1) + 4) // 6 - 1) // k + 1)
    return [2, 3] + [3*i + 1 | 1 for i in range(1, n // 3-correction) if sieve[i]]
    
def primefactors(n, prime_list):
    if n in prime_list:
        return [n]
    results = []
    sqrtn = math.sqrt(n)
    for p in prime_list:
        dm = divmod(n, p)
        if not dm[1]:
            results += [p]
        if sqrtn < p:
            break
    return results    
    
def sumdigits(n):
    total = 0
    for c in str(n):
        total += int(c)
    return total

def totient(n, prime_list):
    for p in primefactors(n, prime_list):
        n *= 1 - 1/p
    return int(n)
        
def tri(x):
    n = int(x)
    return n * (n + 1) // 2

def unhept(n):
    x = int(n)
    return (math.sqrt(9 + 40 * n) + 3) / 10

def unhexag(n):
    x = int(n)
    return (math.sqrt(1 + 8 * n) + 1) / 4

def unoctag(n):
    x = int(n)
    return (math.sqrt(4 + 12 * n) + 2) / 6

def unpent(n):
    x = int(n)
    return ((math.sqrt(1 + 24 * x) - 1) / 2 + 1) / 3

def untri(x):
    n = int(x)
    return (math.sqrt(1 + 8 * n) - 1) / 2 