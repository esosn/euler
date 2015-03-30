import time
import math
from functions import ispandigital
times = []
times.append(time.clock())
limit = 1000

# producing a 9 digit identity means one of the multiplicands must be
# 3 or 4 digits; the other 1/2 or 1, respectively

products = set()

for i in range(2, 99):
    for j in range(123, 988):
        ij = i * j
        identity = str(i) + str(j) + str(ij)
        if ispandigital(identity):
            products.add(ij)
for i in range(2, 10):
    for j in range(1234, 9877):
        ij = i * j
        identity = str(i) + str(j) + str(ij)
        if ispandigital(identity):
            products.add(ij)
            
print(sum(products))

times += [time.clock()]
print(times[-1] - times[-2])