# ДЗ 6.3. Добуток чисел

n = int(input("Введіть число для добутка: "))

n = abs(n)

while n > 9:
    prod = 1
    for ch in str(n):
        prod *= int(ch)
    n = prod

print(n)
