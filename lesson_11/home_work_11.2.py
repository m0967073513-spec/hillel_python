
# 11.2. Заповнення списку кубами чисел

from itertools import takewhile, count

def generate_cube_numbers(end):
    cubes = (n**3 for n in count(2))
    print(takewhile(lambda x: x <= 100, (n**3 for n in count(2))))
    return takewhile(lambda x: x <= end, cubes)

gen = generate_cube_numbers(1)

assert list(generate_cube_numbers(10)) == [8], 'Test1'
print(list(generate_cube_numbers(10)))
assert list(generate_cube_numbers(100)) == [8, 27, 64], 'Test2'
print(list(generate_cube_numbers(100)))
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], 'Test3'
print(list(generate_cube_numbers(1000)))
print('Ok')
