import time
import math
import re
times = []
times.append(time.clock())

fo = open('p013.txt')
data = [int(n) for n in re.split(r'\s*',fo.read())]
fo.close()
print(str(sum(data))[0:10])
 
times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])