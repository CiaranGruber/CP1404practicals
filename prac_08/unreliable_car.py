"""
Create the UnreliableCar class

Unreliable Car Class. Created by Ciaran Gruber - 22/09/18
"""

import random
from prac_08.car import Car


class UnreliableCar(Car):
    """Represent an UnreliableCar object"""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Have a chance of driving the UnreliableCar depending on its reliability"""
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
