import string


UPPER = 127
LOWER = 33


def main():
    """Convert select character and ASCII codes and display table"""
    character = get_character()
    ascii_code = ord(character)
    print('The ASCII code for {} is {}'.format(character, ascii_code))

    ascii_code = get_integer('Please enter a number between {} and {}: '.format(LOWER, UPPER),
                             'Input must be an integer', 'Input must be within {} and {}'.format(LOWER, UPPER),
                             LOWER, UPPER)
    character = chr(ascii_code)
    print('The character for {} is {}'.format(ascii_code, character))
    print()

    columns = get_integer('How many columns? ', 'Column count must be an integer', 'Must be no more than 6 columns', 1, 6)
    print()
    print()
    create_table_header(columns)
    create_data_table(columns)


def create_table_header(columns):
    """Create table header for ASCII table"""
    for x in range(columns):
        print('{:^6}|{:^11}|'.format('Code', 'Character'), end='')
    print()
    for x in range(columns):
        print('------|-----------|', end='')
    print()


def create_data_table(columns):
    """Create data for ASCII table"""
    count = 1
    for x in range(LOWER, UPPER + 1):
        if count == columns:
            print('{:^6}|{:^11}|'.format(x, chr(x)))
            count = 1
        else:
            print('{:^6}|{:^11}|'.format(x, chr(x)), end='')
            count += 1


def get_character():
    """Get a character from user"""
    character = input('Please enter a character: ')
    while character not in string.ascii_letters:
        print('Character must be from character list - {}'.format(string.ascii_letters))
        character = input("Please enter a character: ")
        print()
    return character


def get_integer(prompt, error_prompt, limits_prompt, min_num=-float('inf'), max_num=float('inf')):
    """Get an integer"""
    while True:
        try:
            integer = int(input(prompt))
            if max_num >= integer >= min_num:
                return integer
            print()
            print(limits_prompt)
        except ValueError:
            print()
            print(error_prompt)
        print()


main()
