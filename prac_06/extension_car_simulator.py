from prac_06.car import Car


MENU = """Menu:
d) drive
r) refuel
q) quit"""


def main():
    print("Let's drive!")
    car = Car(input('Enter your car name: '), 100)
    print(car)
    print(MENU)
    menu_choice = input('Enter your choice: ')
    while menu_choice != 'q':
        if menu_choice == 'd':
            distance = get_integer('How many km do you wish to drive? ', 'Distance must be an integer',
                                   'Distance must be >= 0', 0)
            print('The car drove {}km{}'.format(car.drive(distance), (' and ran out of fuel', '')[bool(car.fuel)]))
        elif menu_choice == 'r':
            units_of_fuel = get_integer('How many units of fuel do you want to add to the car? ',
                                        'Fuel must be an integer', 'Fuel amount must be >= 0', 0)
            car.add_fuel(units_of_fuel)
            print('Added {} units of fuel'.format(units_of_fuel))
        elif menu_choice != 'q':
            print('Invalid choice')
        print()
        print(car)
        print(MENU)
        menu_choice = input('Enter your choice: ')
    print("Good bye {}'s driver".format(car.name))


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