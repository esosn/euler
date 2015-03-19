import time
import math
times = []
times.append(time.clock())
limit = 1000

words = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six', \
7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen', \
14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen', \
19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty', \
70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'onethousand'}

total = 0
for i in range(1,limit):
    if i >= 100:
        total += len(words[i // 100])
        total += len(words[100])
        if i % 100 != 0: 
            total += 3 # hundred 'and'
    i = i % 100
    if i <= 20:
        total += len(words[i])
    else:
        total += len(words[(i // 10) * 10])
        i = i % 10
        total += len(words[i])
total += len(words[limit])
print(total)

times.append(time.clock())
print(times[len(times)-1]-times[len(times)-2])
