# implementation of the deterministic Miller-Rabin primality test for small n
# optimised via memoization
# http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

import math
from functions import sundaram

mr_known_values = {x:True for x in sundaram(10000)}

def iswitness(n, a, d, s):
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for i in range(s-1):
        x = pow(x, 2, n)
        if x == 1:
            return True
        if x == n - 1:
            return False
    return True
    
def decompose(n):
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    return d, s

def mr(n):
    d, s = decompose(n)
    if any(iswitness(n, a, d, s) for a in getbases(n)):
        return False
    return True

def isprime(n):
    if n < 2:
        return False
    if n in mr_known_values:
        return mr_known_values[n]
    result = mr(n)
    mr_known_values[n] = result
    return result
    
def getbases(n):
    if n < 2047:
        return (2,)
    if n < 1373653:
        return (2, 3)
    if n < 9080191:
        return (31, 73)
    if n < 25326001:
        return (2, 3, 5)
    if n < 4759123141:
        return (2, 7, 61)
    if n < 1122004669633:
        return (2, 13, 23, 1662803)
    if n < 2152302898747:
        return (2, 3, 5, 7, 11)
    if n < 3474749660383:
        return (2, 3, 5, 7, 11, 13)
    if n < 341550071728321:
        return (2, 3, 5, 7, 11, 13, 17)
    if n >= 3825123056546413051:
        raise ValueError('Deterministic MR only valid for n < 3,825,123,056,546,413,051')
    return (2, 3, 5, 7, 11, 13, 17, 19, 23)