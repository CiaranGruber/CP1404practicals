"""
Create the Bomb class with a superclass of Car

Bomb Class. Created by Ciaran Gruber - 22/09/18
"""

from prac_08.car import Car


class Bomb(Car):
    """Represent a Bomb object"""

    def __init__(self, name, fuel):
        """Initialise a Bomb instance"""
        super().__init__(name, fuel)

    def drive(self, distance):
        """Drive the Bomb car"""
        if distance > self.fuel:
            self.fuel = 0
        else:
            self.fuel -= distance
