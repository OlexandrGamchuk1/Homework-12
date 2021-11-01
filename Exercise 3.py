class Group:
    def __init__(self, students=None):
        if students is None:
            self.students = []
        else:
            self.students = students

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def find_a_student(self, surname):
        for student in self.students:
            if student == surname:
                return student

    def __str__(self):
        self.result = ''
        self.numbers = 0
        for i in self.students:
            self.numbers += 1
            self.result += f'{self.numbers}.{i}\n'
        return self.result


harris = 'Harris Jessica'
ivanov = 'Ivanov Ivan'
adamson = 'Adamson Samuel'
evans = 'Evans Joseph'
smith = 'Smith Olivia'
walker = 'Walker Emily'
davies = 'Davies Thomas'
wilson = 'Wilson George'
king = 'King Lily'

group = [harris, ivanov, adamson, evans, smith, walker, davies, wilson, king]
group = Group(group)
print(group)
lewis = 'Lewis Isabella'
group.add_student(lewis)
print(group)
group.remove_student(ivanov)
print(group)
print(group.find_a_student(adamson))