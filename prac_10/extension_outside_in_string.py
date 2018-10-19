"""
Print a string starting from the outside and working inwards using recursion

Outside to in string recursion. Created by Ciaran Gruber - 19/10/18
"""


def print_outwards_inwards(string):
    """Print from the outside of the string inwards"""
    print(string[0], end='')
    if len(string) > 2:
        print(' ' + string[-1] + ' ', end='')
        print_outwards_inwards(string[1:-1])
    elif len(string) == 2:
        print(' ' + string[1], end='')


if __name__ == '__main__':
    print_outwards_inwards('Programming')
