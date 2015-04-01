import time
import math
import re
times = []
times.append(time.clock())

fo = open('p013.txt')
data = sum(int(n) for n in re.split(r'\s*', fo.read()))
fo.close()
print( str(data)[:10] )
 
times.append(time.clock())
print(times[-1] - times[-2])