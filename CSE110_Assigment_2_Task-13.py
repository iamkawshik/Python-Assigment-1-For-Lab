a = int(input())
c=0
for i in range(1,a+1):
    if a%i==0:
        c+=1
        if i==a:
           print(i)
        else:
            print(i,end=",")
print("Total "+str(c)+" divisors.")