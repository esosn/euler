import time
import math
from functions import gcd
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

denom = denom // gcd(num, denom)

print(denom)

times.append(time.clock())
print(times[-1] - times[-2])