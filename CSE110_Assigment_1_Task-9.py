a = int(input())
b = a/3600
c = a%3600/60
d = (a%3600)%60
print("Hours:",+int(b),"Minutes:",+int(c), "Seconds:",+int(d))