"""
Create table of user-entered people using person class

My Guitars! Created by Ciaran Gruber - 28/08/18
"""

from operator import attrgetter


class Person:
    def __init__(self, first_name='', last_name='', age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return '{} {}. Age={}'.format(self.first_name, self.last_name, self.age)


def main():
    people = []
    first_name = input('First name: ')
    while first_name != '':
        last_name = input('Last name: ')
        age = get_integer('Age: ', 'Age must be an integer', 'Age must be > 0', 0)
        people.append(Person(first_name, last_name, age))
        print()
        first_name = input('First name: ')
    print()
    people.sort(key=attrgetter('age'))
    create_table(['First name', 'Last name', 'Age'], people)


def create_table(header, people):
    column_widths = get_largest_parts(people, header)
    for x in range(3):
        print('{:_<{}s}'.format('', column_widths[x] + 3), end='')
    print()
    for i, title in enumerate(header):
        print('| {:{}} '.format(title, column_widths[i]), end='')
    print('|')
    for x in range(3):
        print('|{:_<{}s}'.format('', column_widths[x] + 2), end='')
    print('|')

    for person in people:
        print('| {:^{}} '.format(person.first_name, column_widths[0]), end='')
        print('| {:^{}} '.format(person.last_name, column_widths[1]), end='')
        print('| {:^{}} '.format(person.age, column_widths[2]), end='')
        print('|')
        for x in range(3):
            print('|{:-<{}s}'.format('', column_widths[x] + 2), end='')
        print('|')


def get_largest_parts(people, header):
    longest_widths = [0, 0, 0]
    for person in people:
        if len(person.first_name) > longest_widths[0]:
            longest_widths[0] = len(person.first_name)
        if len(person.last_name) > longest_widths[1]:
            longest_widths[1] = len(person.last_name)
        if len(str(person.age)) > longest_widths[2]:
            longest_widths[2] = len(str(person.age))
    if len(header[0]) > longest_widths[0]:
        longest_widths[0] = len(header[0])
    if len(header[1]) > longest_widths[1]:
        longest_widths[1] = len(header[1])
    if len(header[2]) > longest_widths[2]:
        longest_widths[2] = len(header[2])
    return longest_widths


def get_integer(prompt, error_prompt, limit_prompt, min_num=0 - float('inf'), max_num=float('inf')):
    valid_input = False
    number = None
    while not valid_input:
        try:
            number = int(input(prompt))
            if not min_num <= number <= max_num:
                print(limit_prompt)
            else:
                valid_input = True
        except ValueError:
            print(error_prompt)
    return number


main()
