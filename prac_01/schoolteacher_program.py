import math


MENU = """(E)ven numbers
(O)dd numbers
(S)quare numbers
(Q)uit"""
x = int(input("First number: "))
y = int(input("Second number: "))
print()
choice = ""
while choice != "Q":
    print(MENU)
    choice = input("Menu choice: ").upper()
    print()
    if choice == "E":
        for a in range(x, y):
            if a % 2 == 0:
                print(a, end=', ')
        print()
    elif choice == "O":
        for a in range(x, y):
            if a % 2 == 1:
                print(a, end=', ')
        print()
    elif choice == "S":
        for a in range(x, y):
            if round(math.sqrt(a)) == math.sqrt(a):
                print(a, end=', ')
        print()
    elif choice != "Q":
        print("Invalid choice")
    print()
