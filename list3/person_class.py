import datetime


class DateOfBirth:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year


class Person:
    def __init__(self, name: str, country: str, dob: DateOfBirth):
        self.name = name
        self.country = country
        self.dob = dob

    def age(self) -> int:
        today = datetime.today()
        birth_date = datetime(self.dob.day, self.dob.month, self.dob.year)
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age
