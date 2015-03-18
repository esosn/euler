import time
import math
times = []
times.append(time.clock())
limit = 10**6 

max = (0,0)
count = 0
known = {13:10,}

def collatz(n):
    global count
    global known
    if n in known:
        count += known[n]
        return
    count += 1
    if n == 1: return
    elif n%2 == 0: collatz(n//2)
    else: collatz(3*n+1)
    
for i in range(2,limit):
    count = 0
    collatz(i)
    known[i] = count
    if max[1] < count: max = (i,count)
print(max[0])

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])