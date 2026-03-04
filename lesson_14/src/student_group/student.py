from __future__ import annotations

from .human import Human


class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return (
            f'Student: {self.first_name} {self.last_name}, '
            f'{self.age} years, {self.gender}, Record book: {self.record_book}'
        )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self) -> int:
        return hash(str(self))