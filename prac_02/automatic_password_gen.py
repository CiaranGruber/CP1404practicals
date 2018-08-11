import string
import random


"""
Automatic password generator that will always give a random password with the desired number of each type of character
"""


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


def main():
    upper_count = get_integer('How many upper characters? ', 'Input must be a number',
                              'Value must be positive and below 100', 0, 100)
    lower_count = get_integer('How many lower characters? ', 'Input must be a number',
                              'Value must be positive and below 100', 0, 100)
    digit_count = get_integer('How many digits? ', 'Input must be a number', 'Value must be positive and below 100', 0,
                              100)
    special_count = get_integer('How many special characters? ', 'Input must be a number',
                                'Value must be positive and below 100', 0, 100)
    total_count = upper_count + lower_count + digit_count + special_count
    password = ''
    for x in range(total_count, 0, -1):
        random_number = random.randint(0, total_count - 1)
        if random_number < upper_count:
            password += random.choice(string.ascii_uppercase)
            upper_count -= 1
        elif random_number < upper_count + lower_count:
            password += random.choice(string.ascii_lowercase)
            lower_count -= 1
        elif random_number < upper_count + lower_count + digit_count:
            password += random.choice(string.digits)
            digit_count -= 1
        else:
            password += random.choice(string.punctuation)
            special_count -= 1
        total_count -= 1
    print('Password: {}'.format(password))


main()
