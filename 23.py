import time
import math
times = []
limit = 28123 + 1

def isabundant(n): 
    divs = set()
    for x in range(1, int(math.sqrt(n)) + 1):
        dm = divmod(n, x)
        if not dm[1]:
            divs.add(x)
            if dm[0] != n: divs.add(dm[0])
    return sum(divs) > n

# 24 is smallest non-eligible
total = 23 * 24 // 2

times.append(time.clock())

# naive brute force, polynomial time
# times ~4s on i3 550 3.2ghz desktop

abundantlist = [12]
for n in range(13, limit-12):
    if isabundant(n):
        abundantlist.append(n)
abundantset = set(abundantlist)

times.append(time.clock())
print(times[-1] - times[-2])

for n in range(25, limit):
    issum = False
    for a in abundantlist:
        if a > n - 12:
            break
        if n - a in abundantset: 
            issum = True
            break
    if not issum:
        total += n

print(total)

times.append(time.clock())
print(times[-1] - times[-2])