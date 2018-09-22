"""
Test the Taxi class

Taxi Test. Created by Ciaran Gruber - 22/09/18
"""

from prac_08.taxi import Taxi


def main():
    new_taxi = Taxi('Prius', 100)
    new_taxi.drive(40)
    print(new_taxi)
    print('Fare: $' + str(new_taxi.get_fare()))
    new_taxi.start_fare()
    new_taxi.drive(100)
    print(new_taxi)
    print('Fare: $' + str(new_taxi.get_fare()))


main()