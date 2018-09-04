"""
Create the class Date which contains code to add days according to leap years

Date Class. Created by Ciaran Gruber - 28/08/18
"""


class Date:
    """Represent the Date"""

    month_to_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, day, month, year):
        """Initialise date instance"""
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    def __str__(self):
        """Return string version of Date"""
        return 'Date: {}/{}/{}'.format(self.day, self.month, self.year)

    def add_days(self, days):
        """Add a certain amount of days to a date. Includes leap years"""
        while days >= 366 or days >= 365 and not self.is_leap_year():  # Adds years until it can't anymore
            if self.is_leap_year():
                self.year += 1
                days -= 366
            else:
                self.year += 1
                days -= 365
        days += self.day
        self.day = 1
        while days > 0:
            if days > self.month_to_day[self.month] + 1 or days > self.month_to_day[self.month] and \
                    not(self.month == 2 and self.is_leap_year()):
                if self.month == 12:
                    self.month = 1
                    self.year += 1
                else:
                    self.month += 1
                days -= self.month_to_day[self.month]
                if self.month == 2 and self.is_leap_year():
                    days -= 1
            else:
                self.day += days - 1
                days = 0
        return self

    def is_leap_year(self):
        """Return whether date is a leap year"""
        return self.year % 4 == 0 or self.year % 400 == 0 and not self.year % 100 == 0
