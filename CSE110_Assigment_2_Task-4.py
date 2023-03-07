sum1 = 0
sum2 = 0
for i in range(1,600):
    if i%7==0 or i%9 == 0:
        sum1 = sum1+i
    if i%7==0 and i%9 == 0:
        sum2 = sum2+i

print(sum1-sum2)