import math
limit = 10**8

def ispalindrome(x):
    for i in range(len(x)//2):
        if x[i] != x[len(x)-1-i]: return False
    return True

def issum(x):
    n = int(math.ceil(math.sqrt(x)))
    if any(s - x in ssset for s in sslist[:n]): return True
    return False

sslist = list(map(lambda x: int(x*(x+1)*(2*x+1)/6), range(int(math.ceil(math.sqrt(limit))) + 1)))
ssset = set(sslist)
sum = 0
for i in range(2,limit):
    if ispalindrome(str(i)) and issum(i):
        sum += i
print(sum)