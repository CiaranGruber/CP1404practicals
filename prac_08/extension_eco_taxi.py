"""
Create the EcoTaxi class with a superclass of Taxi

EcoTaxi Class. Created by Ciaran Gruber - 22/09/18
"""

from prac_08.taxi import Taxi


class EcoTaxi(Taxi):
    """Represent an EcoTaxi object"""
    eco_discount = 0.3

    def __init__(self, name, fuel):
        """Initialise an EcoTaxi instance"""
        super().__init__(name, fuel)
        self.price_per_km *= 1 - self.eco_discount
    
    def drive(self, distance):
        """Drive the EcoTaxi car"""
        self.fuel += distance / 2
        return super().drive(distance)
