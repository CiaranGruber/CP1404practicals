"""
Test the SilverServiceTaxi class

SilverServiceTaxi class. Created Ciaran Gruber - 22/09/18
"""


from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi('Taxi', 200, 2)
    taxi.drive(18)
    print('Expected $48.78, got $' + str(taxi.get_fare()))


main()
