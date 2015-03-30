import time
import math
from functions import ispandigital
times = []
times.append(time.clock())
    
# concatenating > 1 multiples starting from 1 must yield a 9 digit result
# 0 - 2, 10 - 24, 34 - 99, 334 - 4999, and > 99999 don't work as x
# x = 0 mod 5 can't produce 1-9 pandigitals since n >= 2
# x must start with 9 since answer >= 918273645 and n = 1 is included
# search space is quite small!

largest = 918273645   # x = 9
        
for x in range(91, 100):
    if x % 5 == 0:
        continue
    n = 1
    s = ''
    while len(s) < 9:
        s += str(n * x)
        n += 1
    if ispandigital(s) and int(s) > largest:
        largest = int(s)
        
for x in range(9001, 10000):
    if x % 5 == 0:
        continue
    n = 1
    s = ''
    while len(s) < 9:
        s += str(n * x)
        n += 1
    if ispandigital(s) and int(s) > largest:
        largest = int(s)
        
print(largest)

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])