"""
A simulator that simulates a gopher population in a library

11/08/18 - Created by Ciaran Gruber
"""

import random

REPEATS = 9
STARTING_POPULATION = 1000
MIN_INCREASE = 10
MAX_INCREASE = 20
MIN_DECREASE = 5
MAX_DECREASE = 25


def main():
    population = STARTING_POPULATION
    year = 1
    print('Welcome to the Gopher Population Simulator')
    print('Starting population {}'.format(STARTING_POPULATION))
    print('Year {}'.format(year))
    for x in range(REPEATS):
        increase = round(population * (random.uniform(MIN_INCREASE / 100, MAX_INCREASE / 100)))
        decrease = round(population * (random.uniform(MIN_DECREASE / 100, MAX_DECREASE / 100)))
        population += round(increase - decrease)
        year += 1
        print()
        print('{} gophers were born. {} died'.format(increase, decrease))
        print('Population: {}'.format(population))
        print('Year {}'.format(year))


main()
