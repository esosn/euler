import time
import math
from functions import untri
times = []
times.append(time.clock())

def getvalue(s):
    value = 0
    for c in s:
        x = ord(c)
        if x >= 65 and x <= 90:
            value += x - 64
    return value

fo = open('p042_words.txt')
data = fo.read().split(',')
fo.close()

triwords = 0
for s in data:
    x = untri(getvalue(s))
    if x == int(x):
        triwords += 1
print(triwords)

times.append(time.clock())
print(times[-1] - times[-2])