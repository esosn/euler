import math
# prime algo created by Robert William Hanks
# http://stackoverflow.com/a/3035188/1046207
def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]
    
# sieve of atkin implementation by Zsolt KOVACS
# http://stackoverflow.com/a/27215801/1046207
def atkin(limit):
    P = [2,3]
    sieve=[False]*(limit+1)
    for x in range(1,int(math.sqrt(limit))+1):
        for y in range(1,int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7 : sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
    for x in range(5,int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False
    for p in range(5,limit):
        if sieve[p] : P.append(p)
    return P
    
def t(n):
    return 2*n**2-1
    
print('primes complete')

# transform to dictionary for O(1) contains
ceiling = 10**4
# atkin is slower but more memory efficient
#primeList = primes1(t(ceiling))
primeList = atkin(t(ceiling))
i = iter(primeList)
primes = {primeList[i]: True for i in range(0, len(primeList))}

print('dictionary complete')

# count primes satisfying 2n**2-1
count = 0
for i in range(2,ceiling):
    if(t(i) in primes): count += 1
print(count)