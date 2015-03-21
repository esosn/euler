import time
times = []
times.append(time.clock())
limit = 100

# brute force, O(n2)

seen = set()
for a in range(2, limit + 1):
    for b in range(2, limit + 1):
        seen.add(a ** b)
print(len(seen))

times.append(time.clock())
print(times[-1] - times[-2])