"""
National Register Number generator code for Belgium.
"""


class NrnBelgiumSpecific:
    def __init__(self, year, month, day, number, gender):
        self.year = year
        self.month = month
        self.day = day
        self.number = number
        self.gender = gender

        print(self.year, self.month, self.day, self.number, self.gender)
