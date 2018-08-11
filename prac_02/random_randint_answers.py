# Code
import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

old_num = 5
for x in range(10000000):
    new_num = random.uniform(2.5, 5.5)
    if old_num > new_num:
        old_num = new_num
print(old_num)

# What did you see on line 1?
# Largest number could be 20 while the smallest would be 5

# What did you see on line 2?
# The smallest number I could have seen would be a 3 and the largest would be 9
# This could not have produced a 4

# What did you see on line 3?
# 2.5 is the smallest number possible while 5.5 is the largest number possible