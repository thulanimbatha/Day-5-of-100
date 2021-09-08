# add up the even numbers from 2 - 100

total = 0
# 2 <= num < 101 step size =2
for num in range(2, 101, 2):
    total += num
print(total)