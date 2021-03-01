class Data:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

    def get_full_date(self):
        return f'{self.day}-{self.month}-{self.year}'

    @classmethod
    def day_method(cls,day,month,year):
        cls.day = int(day)
        print(cls.day)

    @staticmethod
    def validation(day,month,year):
        print(f"Число - {day}")
        print(f'Месяц - {month}')
        print(f'Год - {year}')

d1 = Data(26,2,21)
print(d1.get_full_date())
Data.day_method(26,2,21)
Data.validation(26,2,21)

