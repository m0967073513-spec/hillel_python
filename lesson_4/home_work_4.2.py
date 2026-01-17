
# ДЗ 4.2. Знайти суму елементів із парними індексами

number = [3, 1, 5, 8, 1, 10]

even_sum = sum(number[::2])
last = number[-1]
result = even_sum * last

print(result)


number = [2, 3, 5]

if not number:
    result = 0
else:
    i = 0
    even_sum = 0

    while i < len(number):
        even_sum += number[i]
        i += 2

    result = even_sum * number[-1]

print(result)


number = []
i = 0
even_sum = 0

while i < len(number):
    if i % 2 == 0:
        even_sum += number[i]
    i += 1
result = even_sum * number[-1] if number else 0

print(result)
