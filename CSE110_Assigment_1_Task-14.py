a = int(input())
b = int(input())
a = a/1000
b = b/3600
c = a/b
if c<60:
    print("%s km/h"%(c))
    print("Too slow. Needs more changes.")
elif c>=60 and c<=90:
    print("%s km/h"%(c))
    print("Velocity is okay. The car is ready!")
elif c>90:
    print("%s km/h"%(c))
    print("Too fast. Only a few changes should suffice.")