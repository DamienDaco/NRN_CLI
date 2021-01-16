"""
National Register Number generator code for Belgium.
"""


class NrnBelgiumGenerateFromDate:
    def __init__(self, year, month, day, gender):
        self.year = year
        self.month = month
        self.day = day
        self.gender = gender
        self.yearLast2Digits = self.year[2:]

        print(self.year, self.month, self.day, self.gender)



