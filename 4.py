import time
import math
from itertools import product
from functions import ispalindrome
times = []
times.append(time.clock())
limit = 1000

# naive implementation
# worst O(n2), best O(1), average O(n)

max = 0
for i in range(limit - 1, limit // 10 - 1, -1):
    for j in range(limit - 1, i - 1, -1):
        k = i * j
        if ispalindrome(k) and k > max: 
            max = k
print(max)

times.append(time.clock())
print(times[-1] - times[-2])