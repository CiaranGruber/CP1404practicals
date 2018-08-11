"""
Ciaran
"""

MIN_LENGTH = 5


def main():
    """Check password"""
    password = ''
    while not is_min_length(password, MIN_LENGTH):
        password = input('Please type in your password')
        if is_min_length(password, MIN_LENGTH):
            for x in range(len(password)):
                print('*', end='')
        else:
            print('Please type in an appropriate password')


def is_min_length(text, min_length):
    """Check if text is of a minimum length"""
    return len(text) >= min_length


main()
