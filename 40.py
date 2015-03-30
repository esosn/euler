import time
import math
times = []
times.append(time.clock())

result = 1
ds = {x for x in range(7)}
prevlen = 0
for i in range(1, 8): # number of digits
    # calculate length of string
    maxlen = i * (10 ** i - 10 ** (i - 1)) + prevlen
    dlist = sorted(ds)
    # evaluate d(i)s 
    for d in dlist:
        dvalue = 10 ** d
        if dvalue <= maxlen:
            ds.discard(d)
            dm = divmod(dvalue - prevlen, i)
            if dm[1]:
                num = dm[0] + 10 ** (i - 1) # add minimum value in
                mult = int(str(num)[dm[1] - 1])
            else: # really just d(1) case
                mult = int(str(dm[0])[0])
            result *= mult
        else:
            break
    prevlen = maxlen
        
print(result)

times.append(time.clock())
print(times[-1] - times[-2])