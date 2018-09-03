"""
Quick pick lottery generator generates QUICK_PICK_SIZE random numbers between MIN_NUMBER and MAX_NUMBER and shows a list

Lottery Generator. By Ciaran Gruber 14/08/18
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
QUICK_PICK_SIZE = 6


def main():
    quick_pick_amount = get_integer('How many quick picks? ', 'Quick pick count must be an integer',
                                    'Quick pick count must be above 0', 1)
    numbers = []
    for x in range(quick_pick_amount):
        while len(numbers) < QUICK_PICK_SIZE + 1:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in numbers:
                numbers.append(number)
        numbers.sort()
        for a in range(QUICK_PICK_SIZE):
            print(numbers[a], end=' ')
        print()


def get_integer(prompt, error_prompt, limits_prompt, min_num=-float('inf'), max_num=float('inf')):
    """Get an integer"""
    while True:
        try:
            integer = int(input(prompt))
            if max_num >= integer >= min_num:
                return integer
            print()
            print(limits_prompt)
        except ValueError:
            print()
            print(error_prompt)
        print()


main()
