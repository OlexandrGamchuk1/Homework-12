class Human:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def __str__(self):
        return f'Surname: {self.surname.title()}\nName: {self.name.title()}\nAge: {self.age}'


print(Human('ivanov', 'ivan', 19))