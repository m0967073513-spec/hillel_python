from __future__ import annotations

from .exceptions import GroupLimitError
from .student import Student


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number: str):
        self.number = number
        self.group: set[Student] = set()

    def add_student(self, student: Student) -> None:
        if student in self.group:
            return

        if len(self.group) >= self.MAX_STUDENTS:
            raise GroupLimitError(
                f'Неможливо додати більше ніж {self.MAX_STUDENTS} студентів до групи {self.number}'
            )

        self.group.add(student)

    def find_student(self, last_name: str) -> Student | None:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name: str) -> None:
        student = self.find_student(last_name)
        if student is not None:
            self.group.remove(student)

    def __str__(self) -> str:
        all_students = '\n'.join(str(s) for s in self.group)
        return f'Number: {self.number}\n{all_students}\n'