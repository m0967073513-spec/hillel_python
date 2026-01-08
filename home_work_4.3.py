
# ДЗ 4.3. Список із 3 елементів

import random

numbers = []
count = random.randint(3, 10)
result = []
i = 0

while i < count:
    numbers.append(random.randint(1, 10))
    i += 1

print(numbers)
i = 0

while i < len(numbers):
    if i == 0:
        result.append(numbers[i])
    elif i == 2:
        result.append(numbers[i])
    elif i == len(numbers) - 2:
        result.append(numbers[i])
    i += 1

print(result)



# ДЗ 4.3. Список із 3 елементів (кращій варіант на мою думку)

import random

numbers = []
count = random.randint(3, 10)
indexes = [0, 2, -2]
result = []
i = 0

while i < count:
    numbers.append(random.randint(1, 10))
    i += 1

print(numbers)
i = 0

while i < len(indexes):
    result.append(numbers[indexes[i]])
    i += 1

print(result)

