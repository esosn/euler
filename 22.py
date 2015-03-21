import time
times = []
times.append(time.clock())
limit = 10000

# O(n log n) [timsort] + O(n) [summation]; naive
# complexity reduces to O(n log n)

def score(name):
    value = 0
    for l in name:
        if(l.isalpha()): # there are a bunch of " chars
            value += ord(l) - 64
    return value

total = 0
fo = open('p022_names.txt')
raw = fo.read()
fo.close()

names = raw.split(',')
names.sort()
for i in range(len(names)):
    total += score(names[i]) * (i + 1)
print(total)

times.append(time.clock())
print(times[-1] - times[-2])