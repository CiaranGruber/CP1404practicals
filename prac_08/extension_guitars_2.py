"""
Read guitars.csv and display in a tuple

Guitars Extension. Created by Ciaran Gruber - 22/09/18
"""

from prac_08.extension_guitar import Guitar
FILENAME = 'guitars.csv'


def main():
    """Get all the guitars from the file and print them"""
    guitars = get_guitars(FILENAME)
    for guitar in guitars:
        print(guitar)
    print()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def get_guitars(filename):
    """Read the guitar file and return all the guitars"""
    guitars = []
    with open(filename) as guitars_file:
        for guitar_data in guitars_file:
            guitar = tuple(guitar_data.strip().split(','))
            guitars.append(Guitar(guitar[0], int(guitar[1]), float(guitar[2])))
    return guitars


main()
