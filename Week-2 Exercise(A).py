a = input("Enter a list of numbers separated by spaces: ").split()
a = [int(x) for x in a]
if len(a)> 1:
    a[0], a[-1] = a[-1], a[0]
print(a)