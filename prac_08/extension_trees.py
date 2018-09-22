"""
CP1404/CP5632 Practical
Tree class with inherited (specialised tree) classes
by Trevor Andersen
"""
import random
from math import sqrt


class Tree:
    """Represent a tree, with trunk height and a number of leaves."""
    trunk_width = 1
    tree_leaves_per_row = 3

    def __init__(self):
        """Initialise a Tree with trunk_height of 1 and full row of leaves."""
        self._trunk_height = 1
        self._leaves = self.tree_leaves_per_row

    def __str__(self):
        """Return a string representation of the full Tree, e.g.
         ###
         ###
          |
          |    """
        return self.get_ascii_leaves() + self.get_ascii_trunk()

    def get_ascii_leaves(self):
        """Return a string representation of the tree's leaves."""
        result = ""
        if self._leaves % self.tree_leaves_per_row > 0:
            result += "#" * (self._leaves % self.tree_leaves_per_row) + '\n'
        for i in range(self._leaves // self.tree_leaves_per_row):
            result += "#" * self.tree_leaves_per_row + '\n'
        return result

    def get_ascii_trunk(self):
        """Return a string representation of the tree's trunk."""
        result = ""
        # the _ (underscore) variable is a convention for an unused variable
        for _ in range(self._trunk_height):
            result += ' ' * int((self.tree_leaves_per_row - 1) // 2)
            result += '|' * self.trunk_width + '\n'
        return result

    def grow(self, sunlight, water):
        """Grow a tree based on the sunlight and water parameters.
        Randomly grow the trunk height by a number between 0 and water.
        Randomly increase the leaves by a number between 0 and sunlight."""
        self._trunk_height += random.randint(0, water)
        self._leaves += random.randint(0, sunlight)


class EvenTree(Tree):
    """ represent an even tree, one that only grows leaves in full rows """

    def grow(self, sunlight, water):
        """Grow like a normal tree, but fill out each row of leaves."""
        Tree.grow(self, sunlight, water)
        while self._leaves % 3 != 0:
            self._leaves += 1


class UpsideDownTree(Tree):
    """Represent an upside-down tree; like a normal tree, but upside-down."""

    def __str__(self):
        """Return a string representation of the full tree,
        upside-down compared to a normal tree."""
        return self.get_ascii_trunk() + self.get_ascii_leaves()


class WideTree(Tree):
    """Represent a wide tree: grows twice as wide as a normal tree, e.g.
 #####
 ######
 ######
   ||
   ||  """
    def __init__(self):
        super().__init__()
        self.tree_leaves_per_row *= 2
        self.trunk_width *= 2


class QuickTree(Tree):
    """Represent a tree that grows more quickly."""

    def grow(self, sunlight, water):
        self._trunk_height += water
        self._leaves += sunlight


class FruitTree(Tree):
    """Represent a tree that has fruit as well as leaves, e.g.
.
...
##
###
###
 |
 |  """

    def __init__(self):
        super().__init__()
        self._fruit = 1

    def __str__(self):
        return self.get_ascii_fruit() + super().__str__()

    def get_ascii_fruit(self):
        result = ""
        if self._fruit % self.tree_leaves_per_row > 0:
            result += "." * (self._fruit % self.tree_leaves_per_row) + '\n'
        for i in range(self._fruit // self.tree_leaves_per_row):
            result += "." * self.tree_leaves_per_row + '\n'
        return result

    def grow(self, sunlight, water):
        super().grow(sunlight, water)
        self._fruit += random.randint(0, 1)
        if not random.randint(0, 5):
            self._fruit -= 1


class PineTree(Tree):
    """Represent a pine tree, e.g.
   *
  ***
 *****
*******
   |
   |    """

    def __init__(self):
        super().__init__()
        self._leaves = 4
        self._trunk_height = 1

    def get_ascii_leaves(self):
        result = ""
        levels = int(sqrt(self._leaves))
        for x in range(levels):
            result += ' ' * (levels - x - 1) + '#' * ((x + 1) * 2 - 1) + '\n'
        return result

    def get_ascii_trunk(self):
        result = ""
        for _ in range(self._trunk_height):
            result += ' ' * (int(sqrt(self._leaves)) - 1)
            result += '|' * self.trunk_width
            result += ' \n'
        return result

    def grow(self, sunlight, water):
        if random.randint(0, sunlight) > 2:
            self._leaves += sqrt(self._leaves) * 2 - 1
        self._trunk_height += random.randint(0, water)
