"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# DoneTODO: 1. write down what you think the output of this will be: 3
# print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n > 0:
        print(n ** 2)
        do_something(n - 1)
        print(n ** 2)


"""
DoneTODO: 3. write down what you think the output of do_something(4) will be. Edited: (when fixed)

16
9
4
1
"""
do_something(4)
