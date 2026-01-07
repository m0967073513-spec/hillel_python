
# ДЗ 4.1. Перемістити всі нулі до кінця списку


numbers = [0, 1, 0, 12, 3]
i = 0
end = len(numbers)

while i < end:
    if numbers[i] == 0:
        numbers.pop(i)
        numbers.append(0)
        end -= 1
    else:
        i += 1

print(numbers)


numbers = [0]
i = 0
end = len(numbers)

while i < end:
    if numbers[i] == 0:
        numbers.pop(i)
        numbers.append(0)
        end -= 1
    else:
        i += 1

print(numbers)


numbers = [0, 43, 54, 3, 56, 1, 0, 20 , 39, 7]
i = 0
end = len(numbers)

while i < end:
    if numbers[i] == 0:
        numbers.pop(i)
        numbers.append(0)
        end -= 1
    else:
        i += 1

print(numbers)
