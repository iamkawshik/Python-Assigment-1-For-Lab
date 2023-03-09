a = int(input())
b=0
for i in range(1,a+1):
    if a%i==0:
        b+=1
if b==2:
    print(str(i)+" is a prime number")
else:
    print(str(i)+" is not a prime number")