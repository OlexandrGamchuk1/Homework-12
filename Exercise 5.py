class Date:
    __months = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль',
                8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

    def __init__(self, day, month, year):
        if not isinstance(day, int):
            raise
        if day < 1 or 31 < day:
            raise
        if not isinstance(month, int):
            raise
        if month < 1 or 12 < month:
            raise
        if not isinstance(year, int):
            raise
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year} и {self.day} ' \
               f'{self.__months.get(self.month)} {self.year}'

date = Date(1, 12, 2020)
print(date)