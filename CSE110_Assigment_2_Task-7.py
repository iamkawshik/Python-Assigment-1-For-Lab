c = 0
sum = 0
odd= 0
for i in range(0,10):
    i = int(input())
    if i%2!=0:
        c = c+1
        sum = sum+i
odd = sum/c
print("The total of the odd numbers is %s and their average is %s"%(sum,odd))
