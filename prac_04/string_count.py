def main():
    """Prints any doubled strings given by the user to the console"""
    doubled_strings = get_doubled_input()
    if len(doubled_strings) > 0:
        print('Repeated strings:', end=' ')
        display_list(doubled_strings)
    else:
        print('No repeated strings')


def display_list(a_list):
    """Displays a list to the user separated by commas"""
    for list_item in a_list:
        print(list_item + ',', end=' ')


def get_doubled_input():
    """Returns a list of any strings that the user has inputted more than once"""
    string = '1'
    entered_strings = []
    doubled_strings = []
    while string != '':
        string = input('String: ')
        if string != '' and string in entered_strings and string not in doubled_strings:
            doubled_strings.append(string)
        entered_strings.append(string)
    return doubled_strings


main()
