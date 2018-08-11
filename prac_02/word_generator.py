"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
keep_going = True
menu_choice = 'W'
word_format = "%%#%##%"
MENU = ["""Menu:
 - (W)ord format
 - (C)reate word
 - (Q)uit""", """Menu:
 - (R)andom format
 - (C)hosen format
 - (D)isplay format"""]

while menu_choice != 'Q':
    print(MENU[0])
    menu_choice = input('Menu Choice: ').upper()
    print()
    if menu_choice == 'W':
        print(MENU[1])
        menu_choice = input('Menu Choice: ').upper()
        print()
        if menu_choice == 'R':
            word_format = ''
            for x in range(random.randint(3, 13)):
                if random.randint(0, 2) > 0:
                    word_format += '%'
                elif random.randint(0, 2) > 0:
                    word_format += '#'
                elif not random.randint(0, 3):
                    word_format += random.choice(VOWELS)
                else:
                    word_format += random.choice(CONSONANTS)
            print()
            print('Format: {}'.format(word_format))
            print()
        elif menu_choice == 'C':
            print('Use % for consonants, # for vowels and other letters for set letters')
            word_format = input('Format: ')
            print()
        elif menu_choice == 'D':
            print('Format: {}'.format(word_format))
            print()
    elif menu_choice == 'C':
        word = ''
        for kind in word_format:
            if kind == '%':
                word += random.choice(CONSONANTS)
            elif kind == '#':
                word += random.choice(VOWELS)
            else:
                word += kind
        print(word)
        print()
    elif menu_choice != 'Q':
        print('Invalid choice')
        print()
