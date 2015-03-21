import time
import math
times = []
times.append(time.clock())

limit = 10 ** 8
root = int(math.ceil(math.sqrt(limit)))

def ispalindrome(n):
    x = str(n)
    return x == x[::-1]

def issum(x):
    if any(s - x in ssset for s in sslist[:root]):
        return True
    return False


# precompute for speed; takes ~10ms
sslist = [ int(x * (x + 1) * (2 * x + 1) / 6) for x in range(root) ]
ssset = set(sslist)

times.append(time.clock())
print(times[-1] - times[-2])

# naive solution, does way too much checking for sums
# takes 2-4 minutes, but generates no duplicates
# summation = 0
# for i in range(2, limit):
#     if ispalindrome(str(i)) and issum(i):
#         summation += i
# print(summation)
# 
# times.append(time.clock())
# print(times[-1] - times[-2])

# cutting down on the number of comparisons really speeds it up (~1-2s)
# but it's tricky: there's dupes and singletons (eg 4=2**2) to contend with
summation = 0
found = set((0, 1))

for i2 in range(1, len(sslist)):
    i = sslist[i2]
    for j in sslist[i2 + 2:]:
        x = j - i
        if x > limit:
            break
        if x > 1 and x not in found and ispalindrome(x):
            found.add(x)
            summation += x
    # direct sums (j == 0) are missing
    if i2 > 1 and i not in found and ispalindrome(i):
        found.add(i)
        summation += i
        
print(summation)
times.append(time.clock())
print(times[-1] - times[-2])