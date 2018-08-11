"""
Ciaran
"""

MIN_LENGTH = 5


def main():
    """Check password"""
    password = get_password()
    print_password(password)


def print_password(password):
    """Print password"""
    for x in range(len(password)):
        print('*', end='')
    print()


def get_password():
    """Get the password"""
    password = input('Please type in your password')
    while not is_min_length(password, MIN_LENGTH):
        print('Please type in an appropriate password')
        print()
        password = input('Please type in your password')
        print()
    return password


def is_min_length(text, min_length):
    """Check if text is of a minimum length"""
    return len(text) >= min_length


main()
