import time
import math
times = []
times.append(time.clock())

# 1900-1-1 is monday, but count from 1901-1-1
curday = 1+365
sundays = 0
for year in range(1,101):
    if curday % 7 == 0: sundays += 1
    curday += 31
    if curday % 7 == 0: sundays += 1
    curday += 28 if year % 4 != 0 or not (year % 400 != 0 and year % 100 == 0) else 29
    if curday % 7 == 0: sundays += 1
    curday += 31
    if curday % 7 == 0: sundays += 1
    curday += 30
    if curday % 7 == 0: sundays += 1
    curday += 31
    if curday % 7 == 0: sundays += 1
    curday += 30
    if curday % 7 == 0: sundays += 1
    curday += 31
    if curday % 7 == 0: sundays += 1
    curday += 31
    if curday % 7 == 0: sundays += 1
    curday += 30
    if curday % 7 == 0: sundays += 1
    curday += 31
    if curday % 7 == 0: sundays += 1
    curday += 31
    if curday % 7 == 0: sundays += 1
    curday += 31
print(sundays)

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])