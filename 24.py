import time
import math
from queue import PriorityQueue
times = []
times.append(time.clock())

limit = 1000000

# count the number of choices represented by fixing most significant digit
# search based on desired index value
# 9! * 0 = 0 < 1000000 : 0
# 9! * 1 = 362880 < 1000000 : 1
# 9! * 2 = 725760 < 1000000 : 2
# 9! * 3 = 1088640 > 1000000 : 3 -> #1m starts with 2

digits = set(range(10))
result = ''
iterationvalue = 0

def choose():
    global iterationvalue, result, digits
    size = len(digits)
    sdigits = sorted(digits)
    if size == 1:
        result += str(sdigits[0])
        print(result)
        return
    for i in range(size):
        numpermutations = math.factorial(size - 1) * (i + 1)
        if numpermutations + iterationvalue >= limit:
            result += str(sdigits[i])
            digits.discard(sdigits[i])
            iterationvalue += math.factorial(size - 1) * (i)
            choose()
            return
        
choose()

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])