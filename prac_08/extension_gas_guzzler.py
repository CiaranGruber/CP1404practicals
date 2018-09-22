"""
Create the GasGussler class with a superclass of Car

GasGussler Class. Created by Ciaran Gruber - 22/09/18
"""

from prac_08.car import Car


class GasGussler(Car):
    """Represent a GasGussler object"""

    def __init__(self, name, fuel):
        """Initialise a GasGussler instance"""
        super().__init__(name, fuel)

    def drive(self, distance):
        """Drive the GasGussler car"""
        if distance > self.fuel:
            self.fuel /= 2
        else:
            self.fuel -= distance / 2
        return super().drive(distance)
