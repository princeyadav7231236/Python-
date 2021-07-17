class date:
    def __init__(self, year , month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def split_from_dash(cls, string):
        return cls(*string.split("-"))


date1 = date.split_from_dash("2021-7-17")
print(date1.day)
print(date1.month)
print(date1.year)
print(date1.day, date1.month, date1.year)