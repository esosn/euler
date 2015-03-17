import math
import time

def ispalindrome(n):
    x = str(n)
    return x == x[::-1]

def issum(x):
    n = int(math.ceil(math.sqrt(x)))
    if any(s - x in ssset for s in sslist[:n]): return True
    return False

limit = 10**8
start = time.clock()

# precompute for speed; takes ~10ms
sslist = [int(x*(x+1)*(2*x+1)/6) for x in range(int(math.ceil(math.sqrt(limit))))]
ssset = set(sslist)

end = time.clock()
print(end-start)

start = time.clock()
# naive solution, does way too much checking for sums
# takes a couple minutes, but generates no duplicates
sum = 0
for i in range(2,limit):
    if ispalindrome(str(i)) and issum(i):
        sum += i
print(sum)

end = time.clock()
print(end-start)

start = time.clock()
# cutting down on the number of comparisons really speeds it up (<1s)
# but it's tricky: there's dupes and singletons (eg 4=2**2) to contend with
sum = 0
found = set((0,1))

for i2 in range(1,len(sslist)):
    i = sslist[i2]
    for j in sslist[i2+2:]:
        x = j - i
        if x > limit: break
        if x > 1 and x not in found and ispalindrome(x):
            found.add(x)
            sum += x
    # direct sums (j == 0) are missing
    if i2 > 1 and i not in found and ispalindrome(i):
        found.add(i)
        sum += i
print(sum)
end = time.clock()
print(end-start)
