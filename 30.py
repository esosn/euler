import time
times = []
times += [time.clock()]
power = 5

# brute force O(n)

max_digit_value = 9 ** power
limit = len(str(max_digit_value)) * max_digit_value

numbers = []
for i in range(2, limit): 
    total = 0
    for c in str(i):
        total += int(c) ** power
        if total > i:
            break
    if total == i:
        numbers += [i]
        
print(sum(numbers))

times += [time.clock()]
print(times[-1] - times[-2])