"""
Allows user to enter PEOPLE_COUNT people into a dictionary with their date of births

21/08/18 - Parallel Lists Extension Work. Created by Ciaran Gruber
"""

PEOPLE_COUNT = 5


def main():
    people_to_birth_date = {}
    for x in range(PEOPLE_COUNT):
        name = input('Name: ')
        date_of_birth = tuple(input('Date of birth (dd/mm/yyyy): ').split('/'))
        people_to_birth_date[name] = date_of_birth
        print()


main()
