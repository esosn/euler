import time
import math
times = []
times.append(time.clock())
limit = 10**6 

max = (0,0)
known = {13:10,}

def collatz(n):
    global known
    if n in known: return known[n]
    if n == 1: return 1
    elif n%2 == 0: return 1 + collatz(n//2)
    else: return 1 + collatz(3*n+1)
    
for i in range(2,limit):
    count = collatz(i)
    known[i] = count
    if max[1] < count: max = (i,count)
print(max)

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])