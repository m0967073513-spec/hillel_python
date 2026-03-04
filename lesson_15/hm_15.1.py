
# ДЗ 15.1. Клас «Прямокутник»

class Rectangle:

    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def get_square(self):
        return self.width * self.height

    @classmethod
    def from_area(cls, area, base_width=1):
        return cls(base_width, area / base_width)

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        new_area = self.get_square() + other.get_square()
        return Rectangle.from_area(new_area, self.width)

    def __mul__(self, n):
        new_area = self.get_square() * n
        return Rectangle.from_area(new_area, self.width)

    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"
    
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
print(r1)
assert r2.get_square() == 18, 'Test2'
print(r2)
r3 = r1 + r2    
assert r3.get_square() == 26, 'Test3'
print(r3)
r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'
print(r4)
assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'