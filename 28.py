import time
times = []
times.append(time.clock())
n = 1001

# n x n square
# top right corner is n**2
# moving counter clockwise, each corner is prev - (n - 1)

summation = 1 # center is 1
for i in range(3, n + 1, 2):
    i2 = i*i
    summation += 4 * i2 - 6 * (i - 1)
print(summation)

times.append(time.clock())
print(times[-1] - times[-2])