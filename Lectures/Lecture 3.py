import string


def age_checker():
    age = 0
    while age < 1:
        try:
            age = int(input('Age: '))
            if age < 1:
                print('Age must be above 0')
        except ValueError:
            print('Age must be a number')
    if age % 2:
        print('Odd age')
    else:
        print('Even age')


def letter_count(input_string):
    count = 0
    for x in input_string:
        if x in string.ascii_letters:
            count += 1
    return count


print(letter_count('Hello my name is Ciaran'))
