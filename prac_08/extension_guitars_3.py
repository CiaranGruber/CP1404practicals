"""
Read guitars.csv and display in a tuple

Guitars Extension. Created by Ciaran Gruber - 22/09/18
"""

from prac_08.extension_guitar import Guitar


def main():
    """Get all the guitars from the file and print them"""
    guitars = load_guitars('guitars.csv')
    for guitar in guitars:
        print(guitar)
    print()
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    print()
    guitars.append(Guitar(input('Guitar name: '), int(input('Year: ')), float(input('Cost: '))))
    guitars.sort()
    save_guitars('my_guitars.csv', guitars)


def load_guitars(filename):
    """Read the guitar file and return all the guitars"""
    guitars = []
    with open(filename) as guitars_file:
        for guitar_data in guitars_file:
            guitar = tuple(guitar_data.strip().split(','))
            guitars.append(Guitar(guitar[0], int(guitar[1]), float(guitar[2])))
    return guitars


def save_guitars(filename, guitars):
    """Save the guitars to the guitar file"""
    with open(filename, mode='w') as guitars_file:
        for guitar in guitars:
            guitars_file.write(','.join((guitar.name, str(guitar.year), str(guitar.cost))) + '\n')


main()
