"""
Calculate number of blocks required to create a 2D pyramid based upon the number of rows.

2D Pyramid. Created by Ciaran Gruber - 16/10/18
"""

ROW_COUNT = 5


def calculate_pyramid_rows(number_of_rows):
    """Recursively calculate the number of blocks to build a pyramid with a set number of rows"""
    if number_of_rows <= 1:
        return number_of_rows
    return number_of_rows + calculate_pyramid_rows(number_of_rows - 1)


def calculate_pyramid_rows_loop(number_of_rows):
    """With a loop, calculate the number of blocks to build a pyramid with a set number of rows"""
    total_blocks = 0
    for x in range(1, number_of_rows + 1):
        total_blocks += x
    return total_blocks


def main():
    """Calculate total blocks to build a 2D pyramid for ROW_COUNT rows"""
    print('Calculating for {} rows:'.format(ROW_COUNT))
    print()
    print('Recursive function:', calculate_pyramid_rows(ROW_COUNT))
    print('With a loop:', calculate_pyramid_rows_loop(ROW_COUNT))


if __name__ == '__main__':
    main()
