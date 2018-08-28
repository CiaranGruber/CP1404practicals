from prac_06.guitar import Guitar


def main():
    gibson_guitar = Guitar('Gibson L-5 CES', 1922, 16035.40)
    another_guitar = Guitar('Another Guitar', 2012, 2000)
    print('Gibson L-5 CES get_age() - Expected 96. Got', gibson_guitar.get_age())
    print('Another Guitar get_age() - Expected 6. Got', another_guitar.get_age())
    print('Gibson L-5 CES is_vintage() - Expected True. Got', gibson_guitar.is_vintage())
    print('Another Guitar is_vintage() - Expected False. Got', another_guitar.is_vintage())


main()
