"""
Create the SilverServiceTaxi Class

SilverServiceTaxi Class. Created by Ciaran Gruber - 22/09/18
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi object"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance"""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        """Return the string version of a SilverServiceTaxi"""
        return super().__str__() + ' plus flagfall of $' + str(self.flagfall)

    def get_fare(self):
        """Get the current fare"""
        return self.price_per_km * self.current_fare_distance + self.flagfall
