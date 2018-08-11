"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    Value Error will occur if you use a non-integer
2. When will a ZeroDivisionError occur?
    This will occur when the person puts the denominator as a 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    This could be avoided by forcing the user to input a number that is not 0 (eg. while denominator == 0 or not
        denominator)
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while not denominator:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
