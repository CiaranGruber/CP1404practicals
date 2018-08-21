"""
Prints hexadecimal code when user enters colour name.

21/08/18 - Hex Colours. Created by Ciaran Gruber.
"""

COLOURS = {'alice blue': '#f0f8ff', 'antique white': '#faebd7', 'aquamarine 1': '#7fffd4', 'azure 1': '#f0ffff',
           'beige': '#f5f5dc', 'blanched almond': '#ffebcd', 'blue': '#0000FF', 'brown': '#a52a2a',
           'burlywood': '#deb887', 'cadet blue': '#5f9ea0'}


def main():
    """Main code"""
    colour = get_colour()
    while colour != '':
        print("The colour '{}' is {} in hexadecimal code".format(colour, COLOURS[colour.lower()]))
        print()
        colour = get_colour()
    print()
    print('{:^8} | {:^10}'.format('Hex Code', 'Colour'))
    print('{0:_<9s}|{0:_<11s}'.format(''))
    for colour, hex_code in COLOURS.items():
        print('{:8} | {}'.format(hex_code, colour))


def get_colour():
    """Get colour from user input"""
    colour = input('Colour: ')
    while colour.lower() not in COLOURS and colour != '':
        print('Colour not in list')
        colour = input('Colour: ')
    return colour


main()
