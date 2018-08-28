from math import floor


class Date:
    month_to_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, day, month, year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    def __str__(self):
        return 'Date: {}/{}/{}'.format(self.day, self.month, self.year)

    def add_days(self, days):
        while days >= 366 or days >= 365 and not Date.is_leap_year(self):  # Adds years until it can't anymore
            if Date.is_leap_year(self):
                self.year += 1
                days -= 366
            else:
                self.year += 1
                days -= 365
        days += self.day
        self.day = 1
        while days > 0:
            if days > self.month_to_day[self.month] + 1 or days > self.month_to_day[self.month] and \
                    not(self.month == 2 and Date.is_leap_year(self)):
                if self.month == 12:
                    self.month = 1
                    self.year += 1
                else:
                    self.month += 1
                days -= self.month_to_day[self.month]
                if self.month == 2 and Date.is_leap_year(self):
                    days -= 1
            else:
                self.day += days - 1
                days = 0
        return self

    def is_leap_year(self):
        return self.year % 4 == 0 or self.year % 400 == 0 and not self.year % 100 == 0
