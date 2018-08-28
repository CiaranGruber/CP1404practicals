from prac_06.guitar import Guitar


def main():
    guitars = []
    print('My guitars!')
    print()
    name = input('Name: ')
    while name != '':
        year = get_number('Year: ', 'Year must be a number', 'Year must be above 0', 0, 2018, 'int')
        cost = get_number('Cost: ', 'Year must be a number', 'Year must be above 0', 0)
        guitars.append(Guitar(name, year, cost))
        print()
        name = input('Name: ')

    print()
    longest_word = get_largest_name(guitars)
    longest_cost = get_largest_cost(guitars)
    for i, guitar in enumerate(guitars):
        print("Guitar {0}: {self.name:>{1}} ({self.year}), worth ${self.cost:{2},.2f}{3}"
              .format(i + 1, longest_word, longest_cost,
                      ('(vintage)', '')[0 if guitar.get_age() > 50 else 1], self=guitar))


def get_number(prompt, error_prompt, limit_prompt, min_num=0 - float('inf'), max_num=float('inf'), valid_type='either'):
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
    longest_word = 0
    for guitar in guitars:
        if len(guitar.name) > longest_word:
            longest_word = len(guitar.name)
    return longest_word


def get_largest_cost(guitars):
    longest_word = 0
    for guitar in guitars:
        if len(str(guitar.cost)) > longest_word:
            longest_word = len(guitar.name)
    return longest_word


main()
