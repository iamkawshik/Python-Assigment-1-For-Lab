total_sum = 0
for i in range(63, 601, 63):
    if i % 9 == 0:
        total_sum += i
print(total_sum)