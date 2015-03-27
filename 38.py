import time
import math
times = []
times.append(time.clock())

def is19pandigital(s):
    seen = set()
    for c in s:
        if c == '0' or c in seen:
            return False
        seen.add(c)
    return True
    
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
    if len(s) == 9 and is19pandigital(s) and int(s) > largest:
        largest = int(s)
        
for x in range(9001, 10000):
    if x % 5 == 0:
        continue
    n = 1
    s = ''
    while len(s) < 9:
        s += str(n * x)
        n += 1
    if is19pandigital(s) and int(s) > largest:
        largest = int(s)
        
print(largest)

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])