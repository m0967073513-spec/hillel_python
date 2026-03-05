
# ДЗ 14.1. Виняток користувача

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Human: {self.first_name} {self.last_name}, {self.age} years, {self.gender}'


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return (
            f'Student: {self.first_name} {self.last_name}, '
            f'{self.age} years, {self.gender}, Record book: {self.record_book}'
        )

    # для set()
    def __hash__(self):
        return hash(self.record_book)

    def __eq__(self, other):
        return isinstance(other, Student) and self.record_book == other.record_book


# exception
class GroupLimitError(Exception):
    pass


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        # если студент уже есть — просто ничего не делаем
        if student in self.group:
            return

        #  ограничение 10 студентов
        if len(self.group) > self.MAX_STUDENTS:
            raise GroupLimitError(f'Неможливо додати більше ніж {self.MAX_STUDENTS} студентів до групи {self.number}')

        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)  # результат поиска
        if student is not None:
            self.group.remove(student)

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + '\n'
        return f'Number: {self.number}\n{all_students}'

# перехват 11-го студента 

gr = Group('PD1')
for i in range(10):
    gr.add_student(Student('Male', 20 + i, f'Name{i}', f'Last{i}', f'RB{i}'))

print(gr)

# попытка добавить 11-го
try:
    gr.add_student(Student('Female', 30, 'Extra', 'Student', 'RB10'))
except GroupLimitError as e:
    print("Перехоплено виняток:", e)
