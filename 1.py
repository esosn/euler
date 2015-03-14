# O(n). Naive, but simple and easy to understand

total = 0
for i in range(1,1000):
    if i%3 == 0 or i%5 == 0:
        total += i
print(total)

# O(n) but with coefficient 1/3

total = -1 # algo calculates answer + 1
maximum = 1000
threes = maximum // 3
fives = maximum // 5
for i in range(1,max(threes,fives)):
    if(i<=threes):
        total += 3 * i
    if(i<=fives and i%3 != 0):
        total += 5 * i
print(total)