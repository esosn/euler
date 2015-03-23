import time
import math
times = []
times += [time.clock()]
limit = 10**6

def ispalindrome(n):
    x = str(n)
    return x == x[::-1]

# naive search, O(n*m) where m = length of binary string
# cull even choices because binary ends in 0 but can't start with 0
summation = 0
for i in range(1, limit, 2):
    if ispalindrome(i) and ispalindrome(bin(i)[2:]):
        summation += i
print(summation)

times += [time.clock()]
print(times[-1] - times[-2])

# generate binary palindromes and check decimal representations
# if 2**i is in the number, 2**(19-i) must be, by binary palindrome
# number of binary palindromes << value of limit
numbers = {'1','11'}
for i in range(2, int(math.log2(limit)) + 1): # 10**6 < 2**20
    newnums = set()
    for n in numbers:
        if len(n) < i:
            newnums.add('1' + n + '1')
            newnums.add('0' + n + '0')
    s = '1'
    for j in range(i):
        s += '0'
        newnums.add(s + '1')
    numbers.update(newnums)
    
summation = 0
for s in numbers:
    if s[0] == '0': # some strings are generated with prepended 0
        continue
    n = int(s, 2)
    if n < limit and ispalindrome(n):
        summation += n
print(summation)

times += [time.clock()]
print(times[-1] - times[-2])