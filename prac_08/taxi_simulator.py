"""
Simulate a taxi driving program with multiple taxi types

Taxi Simulator. Created by Ciaran Gruber - 22/09/18
"""

from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi

TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
MENU = """Menu:
(D)rive
(C)hoose Taxi
(Q)uit"""


def main():
    current_taxi = None
    bill = 0

    print("Let's Drive!")
    print()
    print(MENU)
    menu_choice = input('>>> ').upper()
    print()
    while menu_choice != 'Q':
        if menu_choice == 'D':
            if current_taxi is not None:
                current_taxi.start_fare()
                current_taxi.drive(get_positive_integer('Drive how far? ', ))
                bill += current_taxi.get_fare()
                print('Your', current_taxi.name, 'trip cost $' + str(current_taxi.get_fare()))
            else:
                print('No car has been chosen')
        else:
            for i, taxi in enumerate(TAXIS):
                print((i + 1), '-', taxi)
            current_taxi = TAXIS[get_positive_integer('Choose Taxi: ', len(TAXIS)) - 1]
        print('Bill to date: $' + str(bill))
        print()
        print(MENU)
        menu_choice = input('>>> ').upper()
        print()


def get_positive_integer(prompt, max_num=float('inf')):
    integer = -1
    while 0 > integer or integer > max_num:
        try:
            integer = int(input(prompt))
            if 0 < integer:
                return integer
            elif 0 > integer:
                print('Number must be > 0')
            else:
                print('Number must be <', max_num)
        except ValueError:
            print('Invalid number')


main()
