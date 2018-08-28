"""
Contain the Guitar class which in turn has name, year and cost

Guitar class. Created by Ciaran Gruber - 28/08/18
"""


class Guitar:
    """Represent a guitar"""

    def __init__(self, name='', year=0, cost=0):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of Guitar"""
        return '{} ({}) : ${}'.format(self.name, self.year, self.cost)

    def get_age(self):
        """Get age of a Guitar"""
        return 2018 - self.year

    def is_vintage(self):
        """Return True if Guitar is vintage"""
        return self.get_age() >= 50
