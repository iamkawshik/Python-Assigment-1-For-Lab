sum=0
for i in range(1,600):
    if i%7==0 and i%9 == 0:
        sum = sum+i
print(sum)