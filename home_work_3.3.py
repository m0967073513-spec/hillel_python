
# ДЗ 3.3. Розділити один список на два списки

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

mid_index = (len(numbers) + 1) // 2
result = [numbers[:mid_index], numbers[mid_index:]]

print(result)
 

numbers = [1, 2, 3]
mid_index = (len(numbers) + 1) // 2
result = [numbers[:mid_index], numbers[mid_index:]]

print(result)


numbers = [1]
mid_index = (len(numbers) + 1) // 2
result = [numbers[:mid_index], numbers[mid_index:]]

print(result)


numbers = []
mid_index = (len(numbers) + 1) // 2
result = [numbers[:mid_index], numbers[mid_index:]]

print(result)
