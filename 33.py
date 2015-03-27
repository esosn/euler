import time
import math
times = []
times.append(time.clock())
limit = 4

found = set()

# seeking ab / bc = a / c < 1
# build the combinations

for i in range(11, 99):
    if i % 10 == 0:
        continue
    num = str(i)
    a = int(num[0])
    b = int(num[1])
    if a < b:
        for j in range(1, 10):
            denom = int(str(b) + str(j))
            if a / j == i / denom:
                found.add((i, denom))
                if len(found) == 4:
                    break
num = 1
denom = 1
for f in found:
    num *= f[0]
    denom *= f[1]

# stein's algorithm
def gcd(u, v):
    if u == 0:
        if v == 0:
            return 0
        return v
    elif v == 0:
        return x
    if u == v:
        return u
    k = 0
    while u != v and u > 0:
        if u % 2 == 0:
            u = u // 2
            if v % 2 == 0:
                v = v // 2
                k += 1
        elif v % 2 == 0:
            v = v // 2
        else:
            if u >= v:
                u = (u - v) // 2
            else:
                newv = u
                u = (v - u) // 2
                v = newv
    return v * 2 ** k

denom = denom // gcd(num, denom)

print(denom)

times.append(time.clock())
print(times[-1] - times[-2])