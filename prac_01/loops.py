for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0, 101, 10):
    print(i, end=' ')
print()
for i in range(20, 0, -1):
    print(i, end=' ')
print()
print()
star_count = int(input("How many stars do you want? "))
for x in range(star_count):
    print("*", end='')
print()
print()
star_count = int(input("How many stars do you want (again)? "))
star_line = ''
for x in range(star_count):
    star_line += '*'
    print(star_line)
print()