NUMBER_COUNT = 5


def main():
    numbers = []
    for x in range(NUMBER_COUNT):
        numbers.append(get_integer('Number: ', 'Input must be a number', 'Input must be within limits'))
    print('The first number is {}'.format(numbers[0]))
    print('The last number is {}'.format(numbers[-1]))
    print('The smallest number is {}'.format(min(numbers)))
    print('The largest number is {}'.format(max(numbers)))
    print('The average of the numbers is {:.1f}'.format(sum(numbers) / len(numbers)))


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
