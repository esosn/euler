import time
import math
times = []
times.append(time.clock())

# 1900-1-1 is monday, but count from 1901-1-1
# sunday = weekday 0
curday = 1 + 365
sundays = 0
for year in range(1, 101):
    # 1
    if curday % 7 == 0:
        sundays += 1
    curday += 31
    # 2
    if curday % 7 == 0:
        sundays += 1
    curday += 28 if year % 4 != 0 or not (year % 400 != 0 and year % 100 == 0) else 29
    # 3
    if curday % 7 == 0:
        sundays += 1
    curday += 31
    # 4
    if curday % 7 == 0:
        sundays += 1
    curday += 30
    # 5
    if curday % 7 == 0:
        sundays += 1
    curday += 31
    # 6
    if curday % 7 == 0:
        sundays += 1
    curday += 30
    # 7
    if curday % 7 == 0:
        sundays += 1
    curday += 31
    # 8
    if curday % 7 == 0:
        sundays += 1
    curday += 31
    # 9
    if curday % 7 == 0:
        sundays += 1
    curday += 30
    # 10
    if curday % 7 == 0:
        sundays += 1
    curday += 31
    # 11
    if curday % 7 == 0:
        sundays += 1
    curday += 31
    # 12
    if curday % 7 == 0:
        sundays += 1
    curday += 31
print(sundays)

times.append(time.clock())
print(times[-1] - times[-2])