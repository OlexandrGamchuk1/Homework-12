class Book:
    def __init__(self, books):
        self.books = books

    def __str__(self):
        list_book = ''
        for book in self.books:
            if 2010 <= book[-2]:
                list_book += f'\t{book}\n'
        return list_book


author = 'Стівен Кінг'
book1 = 'Що впало, те пропало', 'Книжковий клуб "Клуб Сімейного Дозвілля"', 2016, 443
book2 = 'Зона покриття', 'Книжковий клуб "Клуб Сімейного Дозвілля"', 2015, 427
book3 = 'Темна вежа ІІ. Крiзь час', 'Книжковий клуб "Клуб Сімейного Дозвілля"', 2007, 464
books = [book1, book2, book3]
print(f'{author}:\n{Book(books)}')