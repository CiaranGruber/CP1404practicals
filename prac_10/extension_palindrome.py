"""
Check if a word is a palindrome recursively.

Palindrome Check. Created by Ciaran Gruber - 19/10/18
"""

import string


def is_palindrome(input_string):
    """Return if a string is a palindrome"""
    input_string = input_string.lower()
    input_string = ''.join([letter for letter in input_string if letter in string.ascii_lowercase])
    if len(input_string) == 1:
        return True
    elif input_string[0] == input_string[-1]:
        if len(input_string) == 2:
            return True
        else:
            return is_palindrome(input_string[1:-1])
    return False


if __name__ == '__main__':
    print(is_palindrome('A Toyota\'s a Toyota'))
