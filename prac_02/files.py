"""
This file will ask for a name, record it in a text file and proceed to call you by your name
"""

# Recording name
name = input('What is your name? ')
with open('name.txt', mode='w') as file:
    file.write(name)
with open('name.txt') as file:
    name = file.readline()
print('Your name is {}'.format(name))

# Counting numbers
with open('numbers.txt') as file:
    numbers = file.readlines()
total = 0
for x in numbers:
    try:
        total += int(x)
    except ValueError:
        pass
print(total)
