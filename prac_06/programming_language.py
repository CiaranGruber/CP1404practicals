"""
Create ProgrammingLanguage class.

Programming Language class. Created by Ciaran Gruber - 28/08/18
"""


class ProgrammingLanguage:
    """Represent a programming language"""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of ProgrammingLanguage"""
        return '{}, {} Typing, Reflection={}, First appeared in {}'.format(self.name, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self) -> bool:
        """Return if ProgrammingLanguage is Dynamic"""
        return self.typing == 'Dynamic'
