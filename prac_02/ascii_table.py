import string


UPPER = 127
LOWER = 33


def get_integer(prompt, error_prompt, limits_prompt, min_num=0-float('inf'), max_num=float('inf')):
    integer = min_num - 1
    while min_num > integer or integer > max_num:
        try:
            integer = int(input(prompt))
            if min_num > integer or integer > max_num:
                print()
                print(limits_prompt)
                print()
        except ValueError:
            print()
            print(error_prompt)
            print()
    return integer


character = input('Please enter a character: ')
while character not in string.ascii_letters:
    print('Character must be from character list - {}'.format(string.ascii_letters))
    character = input("Please enter a character: ")
    print()
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
for x in range(columns):
    print('{:^6}|{:^11}|'.format('Code', 'Character'), end='')
print()
for x in range(columns):
    print('------|-----------|', end='')
print()
count = 1
for x in range(LOWER, UPPER + 1):
    if count == columns:
        print('{:^6}|{:^11}|'.format(x, chr(x)))
        count = 1
    else:
        print('{:^6}|{:^11}|'.format(x, chr(x)), end='')
        count += 1
