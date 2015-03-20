# O(n log n) [timsort] + O(n) [summation], naive
# complexity reduces to O(n log n)

def score(name):
    value = 0
    for l in name:
        if(l.isalpha()):
            value += ord(l) - 64
    return value

total = 0
fo = open('p022_names.txt')
raw = fo.read()
fo.close()

names = raw.split(',')
names.sort()
for i in range(len(names)):
    total += score(names[i]) * (i+1)
print(total)

