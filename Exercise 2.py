class Human:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age


class Student(Human):
    def __init__(self, surname, name, age, faculty, group):
        super().__init__(surname, name, age)
        self.faculty = faculty
        self.group = group

    def __str__(self):
        return f'Surname: {self.surname.title()}\nName: {self.name.title()}\nAge: {self.age}' \
               f'\nFaculty: {self.faculty.title()}\nGroup: {self.group}'


print(Student('ivanov', 'ivan', 19, 'Educational and Scientific Institute of Economics and Management', '21'))