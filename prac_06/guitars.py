"""
Allow the user to input several guitars and decide whether they're vintage, etc.

My Guitars! Created by Ciaran Gruber - 28/08/18
"""

from prac_06.guitar import Guitar


def main():
    guitars = []
    print('My guitars!')
    print()
    name = input('Name: ')
    while name != '':
        year = get_number('Year: ', 'Year must be a number', 'Year must be above 0 and below 2018', 0, 2018, 'int')
        cost = get_number('Cost: ', 'Cost must be a number', 'Cost must be above 0', 0)
        guitars.append(Guitar(name, year, cost))
        print()
        name = input('Name: ')

    print()
    longest_word = get_largest_name(guitars)
    longest_cost = get_largest_cost(guitars)
    for i, guitar in enumerate(guitars):
        print("Guitar {0}: {1:>{2}} ({3}), worth ${4:{5}.2f}".format(i + 1, guitar.name, longest_word,
                                                                     guitar.year, guitar.cost, longest_cost), end='')
        if guitar.is_vintage():
            print(' (vintage)')
        else:
            print()


def get_number(prompt, error_prompt, limit_prompt, min_num=0 - float('inf'), max_num=float('inf'), valid_type='either'):
    """Require user to input a number which may be a specific type and limited"""
    valid_input = False
    number = None
    while not valid_input:
        try:
            number = input(prompt)
            if valid_type == 'int':
                number = int(number)
            else:
                try:
                    number = int(number)
                except ValueError:
                    number = float(number)

            if not min_num <= number <= max_num:
                print(limit_prompt)
            else:
                valid_input = True
        except ValueError:
            print(error_prompt)
    return number


def get_largest_name(guitars):
    """Find the largest name in a list guitars"""
    longest_word = 0
    for guitar in guitars:
        if len(guitar.name) > longest_word:
            longest_word = len(guitar.name)
    return longest_word


def get_largest_cost(guitars):
    """Find the biggest cost (length) of a list of guitars"""
    longest_word = 0
    for guitar in guitars:
        if len(str(guitar.cost)) > longest_word:
            longest_word = len(guitar.name)
    return longest_word


main()
