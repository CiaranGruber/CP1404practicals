"""
Search Wikipedia pages based upon their title and display the summary.

Wiki Search. Created by Ciaran Gruber - 19/10/18
"""

import wikipedia


def get_integer(prompt, min_num=1, max_num=float('inf')):
    """Get a positive integer within limits"""
    valid_input = False
    menu_option = input(prompt)
    while not valid_input:
        try:
            menu_option = int(menu_option)
            if menu_option < min_num or menu_option > max_num:
                print('Input must be >', min_num, 'and <', max_num)
            else:
                valid_input = True
        except ValueError:
            print('Input must be an integer')
        if not valid_input:
            print()
            print(prompt)
    return menu_option


def main():
    """Prompt user for title and search Wikipedia"""
    print("Wikipedia Search")
    print()
    menu_option = input('Title: ')
    while menu_option.strip() != '':
        print()
        try:
            print(wikipedia.summary(menu_option).strip())
        except wikipedia.exceptions.DisambiguationError as e:
            print(menu_option + ' refers to a disambiguation page. Which page do you wish to choose instead?')
            for i, title in enumerate(e.options):
                print(str(i + 1) + '.', title)
            menu_option = e.options[get_integer('Which page: ', 1, len(e.options)) - 1]
            print()
            print(wikipedia.summary(menu_option).strip())
        print()
        menu_option = input('Title: ')


main()
