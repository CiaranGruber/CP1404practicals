"""
Test the UnreliableCar class to make sure it works properly

UnreliableCar class Test. Created by Ciaran Gruber - 22/09/18
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    new_unreliable_car = UnreliableCar('Unreliable', 100, 10)
    for x in range(10):
        if new_unreliable_car.drive(5) == 0:
            print('Unreliable Car did not drive')
        else:
            print('Unreliable Car drove')

    print()
    new_reliable_car = UnreliableCar('Reliable', 100, 90)
    for x in range(10):
        if new_reliable_car.drive(5) == 0:
            print('Reliable Car did not drive')
        else:
            print('Reliable Car drove')


main()
