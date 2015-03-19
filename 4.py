import time
import math
from itertools import product
times = []
times.append(time.clock())
limit = 1000

def ispalindrome(n):
    x = str(n)
    return x == x[::-1]

# naive implementation
# worst O(n2), best O(1), average O(n)

max = 0
for i in range(limit-1,limit//10-1,-1):
    for j in range(limit-1,i-1,-1):
        k = i*j
        if ispalindrome(k) and k > max: 
            max = k
print(max)

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])