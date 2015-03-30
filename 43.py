import time
import math
from functions import ispandigital, permute
from collections import deque
times = []
times.append(time.clock())

def div_callback(s, *args):
    cb_args = args[-1]
    triplet = int(s[-3:])
    rset = cb_args[1]
    if s[0] != '0' and triplet % cb_args[0] == 0:
        rset.add(s)

def gen_trips(s, p, rset):
    avail_digits = {str(x) for x in range(10)}
    for c in s:
        avail_digits.discard(c)
    permute(s, deque(avail_digits), 0, 1, div_callback, (p, rset))

# seed with triplets = 0 mod 2
results = set()
permute('', deque(str(x) for x in range(10)), 0, 3, div_callback, (2, results))

# generate 9 digit numbers matching divisibility rules
for p in [3, 5, 7, 11, 13, 17]:
    new_results = set()
    for r in results:
        gen_trips(r, p, new_results)
    results = new_results
    
# add msd, check for pandigital, generate results
summation = 0
for s in results:
    avail_digits = {str(x) for x in range(10)}
    for c in s:
        avail_digits.discard(c)
    s = list(avail_digits)[0] + s
    if ispandigital(s, incl_zero = True):
        summation += int(s)

print(summation)

times.append(time.clock())
print(times[-1] - times[-2])