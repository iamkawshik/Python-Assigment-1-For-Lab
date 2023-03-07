a = int(input())
sum1=0
sum2=0
for i in range(1,a+1):
    if i%2==0:
        sum1 = sum1+(i**2)
    if i%2!=0:
        sum2 = sum2+(i**2)
print(sum2-sum1)