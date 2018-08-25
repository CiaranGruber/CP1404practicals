"""
Contains code to convert parallel lists to dictionaries

Convert lists to dictionaries. Created by Ciaran Gruber - 21/08/18
"""


def convert_list_to_dict(keys_list, values_list):
    """Convert two parallel lists into a dictionary"""
    dictionary = dict(zip(keys_list, values_list))
    return dictionary


print(convert_list_to_dict(['John', 'Jack'], [21, 22]))
