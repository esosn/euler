import time
import math
times = []
times.append(time.clock())

# significant pencil and paper analysis done first

num = 2520*11*13*17*19
remainders = []
for i in range(1,21): 
    if num % i != 0: 
        remainders.append((num%i)/i)
for r in remainders:
    num *= r**-1
print(int(num))

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])