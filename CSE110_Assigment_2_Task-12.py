n=int(input())
a=n
c=0
s=0
while a>0:
    a=a//10
    c+=1
while n>0:
    s=(n//(10**c))
    n=(n%(10**c))
    c=c-1
    if(s!=0):
        print(s)